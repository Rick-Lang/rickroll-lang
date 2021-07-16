from sys import argv
from time import time
from os.path import exists
from traceback2 import format_exc


# Help message
rick_help = """
Programming by writing code:   rickroll -s [File_Name]
Generate an audio: rickroll -r [File_Name] -audio [Audio_Name]
Sing code:  rickroll -sing [Audio_Name] [File_Name]

Other Options:
--time:      Show execution time of your code
--help/--h:  Help
"""

# Keywords
KW_print    = 'i_just_wanna_tell_u_how_im_feeling'
KW_if       = 'and_if_u_ask_me_how_im_feeling'

KW_let      = 'give_u_up'
KW_def1     = 'never_knew'
KW_def2     = 'could_feel_this_way'
KW_return1  = 'when_i_give_my'
KW_return2  = 'it_will_be_completely'
KW_main     = 'take_me_to_ur_heart'
KW_end      = 'say_good_bye'

KW_break    = 'desert_u'
KW_continue = 'run_around'
KW_loop     = 'together_forever_and_never_to_part'


keywords = {
    KW_print,
    KW_if,
    KW_let,
    KW_def1,
    KW_def2,
    KW_return1,
    KW_return2,
    KW_main,
    KW_end,
    KW_break,
    KW_continue,
    KW_loop,
}


# Token types
TT_keyword    = 'KEYWORDS'
TT_operator   = 'OPERATORS'
TT_number     = 'VALUE-NUMBER'
TT_bool       = 'VALUE-Bool'
TT_char       = 'VALUE-Char'
TT_string     = 'VALUE-String'

TT_variable   = 'VARIABLE'
TT_function   = 'FUNCTION'
TT_p_variable = 'P_VARIABLE'
TT_p_function = 'P_FUNCTION'


# Set and start a timer
start = time()

# Tokens that the interpreter will totally ignore
ignore_tokens = {'~', "'"}


digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}


seperator = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^'
}


# Operators
OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_relational = {'is', 'is_not', 'is_greater_than', 'is_less_than'}
OP_assignment = {'='}
OP_other      = {'[', ']', '(', ')', '{', '}', ','}

OP_build_in_functions = {'ToString', 'ToInt', 'ToFloat', 'Length'}


variables = []
functions = []

current_line = 0


# Python source code, translated from RickRoll source code
c_code = '#include<iostream>\nusing namespace std;\n'


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

            if char in seperator and quote_count % 2 == 0:

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


    # Convert each token to 
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
        # Variables / Functions
        elif self.tokens[i - 1] == KW_let:
            add_to_parser(TT_variable)
            variables.append(t)

        elif self.tokens[i - 1] == KW_def1:
            add_to_parser(TT_function)
            functions.append(t)


        # Others and possible variables
        elif t in variables or t:
            add_to_parser(TT_variable)



####################################################################################
'Translate To Python'
####################################################################################

def data_type(data):
    pass


class TranslateToPython:

    def __init__(self, types, values):

        # types of the tokens
        self.types = types
        # tokens
        self.values = values

        if self.types:
            if self.types[0] == TT_keyword or self.values[0] in functions:
                # Convert RickRoll code to Python
                self.convert(kw=self.values[0])

            else:
                print(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')
                exit('------'*10 + '\n"You know the rules, and so do I~"')


    def convert(self, kw):

        if kw in functions:
            self.write(f'{join_list(self.values)}')

        if kw == KW_main:
            self.write('int main(int argc, char* argv[]){')

        if kw == KW_print:
            # print EXP

            exp = join_list(self.values[1: len(self.values)])
            self.write(f'cout<<{exp};')

        if kw == KW_let:
            # IDENTIFIER = VALUE
            exp = self.values[1: len(self.values)]

            eql_op_index = 0
            var = ''
            for i in range(len(self.types)):
                if self.values[i] == '=':
                    eql_op_index = i

                if self.types[i] == TT_variable:
                    var = self.values[i]

                if self.types[i] == TT_string:
                    self.write(f'string {var} = {join_list(exp[eql_op_index:len(exp)])};')

                if self.types[i] == TT_number:
                    self.write(f'int {var} = {join_list(exp[eql_op_index:len(exp)])};')

                if self.types[i] == TT_bool:
                    self.write(f'bool {var} = {join_list(exp[eql_op_index:len(exp)])};')


        if kw == KW_if:
            # IF CONDITION:

            condition = join_list(self.values[1: len(self.values)])
            self.write(f'if({condition})' + '{')

        if kw == KW_loop:
            self.write('while(true){')

        if kw == KW_break:
            self.write('break;')

        if kw == KW_continue:
            self.write('continue;')

        if kw == KW_def1:
            arguments = join_list(self.values[2 : len(self.values) - 1])

            self.write(f'char {self.values[1]}({arguments})' + '{')

        if kw == KW_return1:
            exp = join_list(self.values[1: len(self.values) - 1])
            self.write(f'return {exp};')


        if kw == KW_end:
            self.write('}')


    def write(self, stmt):
        global c_code
        c_code += stmt + '\n'




####################################################################################
'Main'
####################################################################################

audio_engine = None

class Main:
    def __init__(self):
        is_help = False
        show_time = False
        src_file_name = ''


        if len(argv) <= 1:
            exit(rick_help)


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            # Run code. -s [file_name]
            if current_arg == '-r':
                src_file_name = argv[i + 1]


            # Help message
            if current_arg == '--help' or current_arg == '--h':
                is_help = True

            # Show execution time
            if current_arg == '--time':
                show_time = True


        # Run the RickRoll program
        if src_file_name:
            self.run(src_file_name)if exists(src_file_name)else exit(f"File [{src_file_name}] doesn't exist...")


        if is_help:
            print(rick_help)


        if show_time:
            print(f'Execution Time: [{time() - start}] sec.')


    def run(self, src_file_name):
        global current_line

        with open(src_file_name, mode='r', encoding='utf-8') as src:

            content = src.readlines()
            content[-1] += '\n'

            for statement in content:  # "statement" is a line of code the in source code
                current_line += 1

                obj = Token(statement)
                TranslateToPython(types=obj.t_types, values=obj.t_values)

        print(c_code)

Main()