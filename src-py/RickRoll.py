from time import time
from os.path import exists
from traceback2 import format_exc

from commonvariables import *
from crickroll import run_in_cpp
# from AudioGenerator import init


# Help message
rick_help = """
Programming by writing code:   rickroll -s [File_Name]
Generate an audio: rickroll -r [File_Name] -audio [Audio_Name]
Sing code:  rickroll -sing [Audio_Name] [File_Name]

Other Options:
--time:      Show execution time ofyour code
--help/--h:  Help
"""


# Token types
TT_keyword  = 'KEYWORDS'
TT_operator = 'OPERATORS'
TT_number   = 'VALUE-NUMBER'
TT_bool     = 'VALUE-Bool'
TT_char     = 'VALUE-Char'
TT_string   = 'VALUE-String'

TT_variable = 'VARIABLE'
TT_function = 'FUNCTION'
TT_library  = 'LIBRARY'


# Set and start a timer
start = time()

# Keywords can execute outside main function
kw_exe_outside_main = {KW_main, KW_def1, KW_import1}

variables = []
functions = []


indent_count = 0    # Determine if needs to indent
current_line = 0

# Is the current statement in main
is_main = False
# Is the current statement in a function
is_function = False


# Python source code, translated from RickRoll source code
py_code = ''

# Store libraries
libraries = {}


# "join_list" is a replacement of ''.join()
def join_list(l):
    result = ''
    for i in l: result += f'{i}'
    return result


####################################################################################
'Token Class'
"""
Token class is used to tokenize a RickRoll statement
"""
####################################################################################
class Token:
    def __init__(self, statement):
        self.statement = statement
        self.tokens = []

        self.tokenize()

        self.t_types = []
        self.t_values = []

        for i in range(len(self.tokens)):
            if self.tokens[i]:
                self.convert_token(i)



    # Split statements to single word / token
    def tokenize(self):

        current_token = ''
        quote_count = 0

        for char in self.statement:

            if char == '"':
                quote_count += 1

            if char == '#':
                break
            if char in ignore_tokens:
                continue

            if char in separators and quote_count % 2 == 0:

                if current_token != ' ' and current_token != '\n':
                    self.tokens.append(current_token)
                if char != ' ' and char != '\n':
                    self.tokens.append(char)

                current_token = ''

            else:
                current_token += char


    # is_num determines whether the token is a number
    def is_num(self, string = ''):
        count = 0
        for i in string:
            if i in digits:
                count += 1

        return True if len(string) == count and string.count('.') <= 1 else False


    # Convert each token
    def convert_token(self, i=0):

        global variables

        def add_to_parser(token_type):
            self.t_types.append(token_type)
            self.t_values.append(self.tokens[i])

        def add_operator(operator_in_python):
            self.t_types.append(TT_operator)
            self.t_values.append(operator_in_python)


        t = self.tokens[i]

        # If the token is a key word
        if t in keywords:
            add_to_parser(TT_keyword)


    # Operators
        # Arithmetic Operators
        elif t in OP_arithmetic or t in OP_assignment or t in OP_other:
            add_to_parser(TT_operator)

        # Relational Operator
        elif t in OP_relational or t in OP_build_in_functions:
            if t == 'is': add_operator('==')
            if t == 'is_not': add_operator('!=')
            if t == 'is_greater_than': add_operator('>')
            if t == 'is_less_than': add_operator('<')

            # Build in functions
            if t == 'ToString': add_operator('str')
            if t == 'ToInt': add_operator('int')
            if t == 'ToFloat': add_operator('float')
            if t == 'Length': add_operator('len')


    # Value
        # number
        elif self.is_num(t):
            add_to_parser(TT_number)

        # Bool
        elif t == 'True' or t == 'False':
            add_to_parser(TT_bool)

        # String
        elif t[0] == '"' and t[-1] == '"':
            add_to_parser(TT_string)


    # Others
        # Variables
        elif self.tokens[i - 1] == KW_let:
            add_to_parser(TT_variable)
            variables.append(t)

        # Library
        elif self.tokens[i - 1] == KW_import1:
            add_to_parser(TT_library)

        # Functions
        elif self.tokens[i - 1] == KW_def1:
            add_to_parser(TT_function)
            functions.append(t)

        # Variables
        elif t and t in variables:
            add_to_parser(TT_variable)

        elif t and t in libraries:
            add_to_parser(TT_library)



####################################################################################
'Translate To Python'
####################################################################################

class TranslateToPython:

    def __init__(self, types, values):

        # types of the tokens
        self.types = types
        # tokens
        self.values = values

        # if there is code in the current line of code
        if self.types:

            if self.types[0] == TT_keyword or self.values[0] in functions or self.values[0] in libraries:
                if is_main or (is_main == False and self.values[0] in kw_exe_outside_main) or is_function:
                    # Convert RickRoll code to Python
                    self.convert(kw=self.values[0])

                else:
                    stdout.write(f'Exception in line {current_line}: [{self.values[0]}] can not be executed outside the main method\n')
                    exit('------'*10 + '\n"You know the rules, and so do I~"')

            else:
                stdout.write(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')
                exit('------'*10 + '\n"If you knew what Im feeling, you would not say no~"')

        # if this line doesn't have code, then write "\n"
        else:
            self.write('')

            
    def convert(self, kw):
        global indent_count
        global is_main
        global is_function
        global libraries

        if kw in functions:
            self.write(f'{join_list(self.values)}')

        if kw == KW_main:
            self.write('if __name__ == "__main__":')

            is_main = True
            indent_count += 1

        if indent_count == 0:
            if is_main: is_main = False
            if is_function: is_function = False

        if kw == KW_print:
            # print EXP

            exp = join_list(self.values[1: len(self.values)])
            self.write(f'print({exp}, end="")')

        if kw == KW_let:
            # IDENTIFIER = VALUE

            exp = join_list(self.values[1: len(self.values)])
            self.write(f'{exp}')

        if kw == KW_if:
            # IF CONDITION:

            condition = join_list(self.values[1: len(self.values)])
            self.write(f'if {condition}:')
            indent_count += 1

        if kw == KW_endless_loop:
            self.write('while True:')
            indent_count += 1

        if kw == KW_while_loop:
            # WHILE CONDITION

            condition = join_list(self.values[1:len(self.values)])
            self.write(f'while {condition}:')
            indent_count += 1

        if kw == KW_break:
            self.write('break')

        if kw == KW_continue:
            self.write('continue')

        if kw == KW_def1:
            arguments = join_list(self.values[2 : len(self.values) - 1])
            self.write(f'def {self.values[1]}({arguments}):')
            is_function = True

            indent_count += 1

        if kw == KW_return1:
            exp = join_list(self.values[1: len(self.values) - 1])
            self.write(f'return {exp}')

        # if kw == KW_import1:
        #     self.write('')

        #     lib_name = join_list(self.values[1: len(self.values)])

        #     try:
        #         with open(f'{lib_name}.rickroll', mode='r', encoding='utf-8') as f:
        #             libraries.update({lib_name : f.read()})

        #     except:
        #         exit(f'Exception in line {current_line}: No library called [{lib_name}]')


        if kw == KW_end:
            self.write('pass')
            indent_count -= 1



    def write(self, stmt):
        global py_code
        py_code += '  ' * indent_count + stmt + '\n'


####################################################################################
'Main'
####################################################################################

audio_engine = None

class Main:
    def __init__(self):
        # is_audio = False
        is_help = False
        show_time = False
        is_cpp = False
        src_file_name = ''


        if len(argv) <= 1:
            exit(rick_help)


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            # Run code. -s [file_name]
            if current_arg == '-r':
                src_file_name = argv[i + 1]

            # Generate audio. -audio [Output audio file name]
            # if current_arg == '-audio':
            #     global audio_engine
            #     is_audio = True

                # audio_engine = init(argv[i + 1])

            if current_arg == '--cpp' or current_arg == '--c++':
                is_cpp = True

            # Help message
            if current_arg == '--help' or current_arg == '--h':
                is_help = True

            # Show execution time
            if current_arg == '--time':
                show_time = True

        # Run the RickRoll program
        if src_file_name:
            if is_cpp:
                run_in_cpp(src_file_name)if exists(src_file_name)else exit(f"File [{src_file_name}] doesn't exist...")

            else:
                run_in_py(src_file_name)if exists(src_file_name)else exit(f"File [{src_file_name}] doesn't exist...")

        else:
            stdout.write('Warning: [Not executing any script...]')


        # if is_audio:
            # self.generate_audio(src_file_name)
            # audio_engine.export()

        if is_help:
            stdout.write(rick_help)

        if show_time:
            stdout.write(f'\nExecution Time: [{time() - start}] sec.')

    # def generate_audio(self, src_file_name):

    #     with open(src_file_name, mode='r', encoding='utf-8') as src:
    #         for statement in src.readlines():
    #             obj = Token(statement)

    #             for i in range(len(obj.t_types)):
    #                 audio_engine.generate(obj.t_values[i])



def run_in_py(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        content[-1] += '\n'

        for statement in content:  # "statement" is a line of code the in source code
            current_line += 1

            obj = Token(statement)
            TranslateToPython(types=obj.t_types, values=obj.t_values)


    # Execute python code
    try:
        exec(py_code, globals(), globals())


    # Return RickRoll exception/error
    except:
        error = format_exc().split('File "<string>",')[-1]
        stdout.write(f'Exception in{error}\n' + '-------'*10+'\n"'+"There ain't no mistaking, is true love we are making~" + '"')


Main()
