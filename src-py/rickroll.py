from sys import argv
from time import time
from os.path import exists
from traceback2 import format_exc


"""
Programming by writing code:   rick -s [File_Name]
Sing code:  rick -sing [MP3_Name] [File_Name]

Options:
-time : Show execution time of your code
-mp3 : Generate a mp3 audio file from your source code

"""


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


TT_keyword    = 'KEYWORDS'
TT_operator   = 'OPERATORS'
TT_int        = 'VALUE-Int'
TT_float      = 'VALUE-Float'
TT_bool       = 'VALUE-Bool'
TT_char       = 'VALUE-Char'
TT_string     = 'VALUE-String'

TT_variable   = 'VARIABLE'
TT_function   = 'FUNCTION'
TT_p_variable = 'P_VARIABLE'
TT_p_function = 'P_FUNCTION'


# Set and start a timer
start = time()


digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}


seperator = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^'
}


OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_relational = {'is', 'is_not', 'is_greater_than', 'is_less_than'}
OP_assignment = {'='}
OP_other      = {'[', ']', '(', ')', '{', '}', ','}

OP_buildin_functions = {'ToString', 'ToInt', 'ToFloat', 'Length'}


variables = []
functions = []


indent_count = 0
current_line = 0


py_code = ''


def join(l):
    result = ''
    for i in l: result += f'{i}'
    return result



####################################################################################
'Token Class'
####################################################################################
class Token:
    def __init__(self, exp):
        self.exp = exp
        self.current_token = ''
        self.quote_count = 0
        self.tokens = []

        self.tokenize()

        self.types = []
        self.values = []

        for i in range(len(self.tokens)):
            if self.tokens[i]:
                self.convert_token(i)



    # Split statements to single word / token
    def tokenize(self):
        for char in self.exp:

            if char == '"':
                self.quote_count += 1

            if char == '#':
                break
            if char == '~':
                continue

            if char in seperator and self.quote_count % 2 == 0:

                if self.current_token != ' ' and self.current_token != '\n':
                    self.tokens.append(self.current_token)
                if char != ' ' and char != '\n':
                    self.tokens.append(char)

                self.current_token = ''

            else:
                self.current_token += char



    def is_digit(self, string = ''):
        count = 0
        for i in string:
            if i in digits:
                count += 1

        if len(string) == count:
            return string.count('.')


    # Convert each token to 
    def convert_token(self, i=0):

        global variables

        def add_to_parser(token_type):
            self.types.append(token_type)
            self.values.append(self.tokens[i])

        def add_operator(operator_in_python):
            self.types.append(TT_operator)
            self.values.append(operator_in_python)


        t = self.tokens[i]

        # If the token is a key word
        if t in keywords:
            add_to_parser(TT_keyword)


    # Operators
        # Arithmetic Operators
        elif t in OP_arithmetic or t in OP_assignment or t in OP_other:
            add_to_parser(TT_operator)

        # Relational Operator
        elif t in OP_relational or t in OP_buildin_functions:
            if t == 'is':
                add_operator('==')

            if t == 'is_not':
                add_operator('!=')

            if t == 'is_greater_than':
                add_operator('<=')

            if t == 'is_less_than':
                add_operator('>=')

            # Build in functions

            if t == 'ToString':
                add_operator('str')

            if t == 'ToInt':
                add_operator('int')

            if t == 'ToFloat':
                add_operator('float')

            if t == 'Length':
                add_operator('len')


    # Value
        # Int
        elif self.is_digit(t) == 0:
            add_to_parser(TT_int)

        # Float
        elif self.is_digit(t) == 1:
            add_to_parser(TT_float)

        # Bool
        elif t == 'TrueLove' or t == 'FalseFalse':
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


        else:
            exit(f'Exception in line {current_line}: <{t}>\n\n"You know the rules, and so do I~"')


####################################################################################
'Translate To Python'
####################################################################################

class TranslateToPython:
    def __init__(self, types, values):

        self.types = types
        self.values = values

        if not self.types:
            # move to next line
            self.write('')


        if (self.types) and (self.types[0] == TT_keyword or self.values[0] in functions):
            self.convert(kw=self.values[0])


            
    def convert(self, kw):
        global indent_count

        if kw in functions:
            self.write(f'{join(self.values)}')


        elif kw == KW_main:
            self.write('if __name__ == "__main__":')

            indent_count += 1


        elif kw == KW_print:
            # print EXP

            exp = join(self.values[1: len(self.values)])
            self.write(f'print({exp}, end="")')


        elif kw == KW_let:
            # IDENTIFIER = VALUE

            exp = join(self.values[1: len(self.values)])
            self.write(f'{exp}')


        elif kw == KW_if:
            # IF CONDITION:

            exp = join(self.values[1: len(self.values)])
            self.write(f'if {exp}:')

            indent_count += 1


        elif kw == KW_loop:
            self.write('while True:')

            indent_count += 1


        elif kw == KW_break:
            self.write('break')


        elif kw == KW_continue:
            self.write('continue')


        elif kw == KW_def1:
            arguments = join(self.values[2 : len(self.values) - 1])

            self.write(f'def {self.values[1]}({arguments}):')

            indent_count += 1


        elif kw == KW_return1:
            exp = join(self.values[1: len(self.values) - 1])
            self.write(f'return {exp}')



        elif kw == KW_end:
            self.write('pass')
            indent_count -= 1


        else:
            self.write('')



    def write(self, stmt):
        global py_code
        py_code += '  ' * indent_count + stmt + '\n'



####################################################################################
'Main'
####################################################################################

class Main:
    def __init__(self):
        self.src_file_name = ''
        self.is_audio = False
        self.show_time = False


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            if current_arg == '-s':
                self.src_file_name = argv[i + 1]

            if current_arg == '-audio':
                self.is_audio = True

            if current_arg == '-time':
                self.show_time = True


        if self.src_file_name:
            self.run()if exists(self.src_file_name)else exit(f"File [{self.src_file_name}] doesn't exist...")



        if self.show_time:
            print(f'Execution Time: [{time() - start}] sec.')



    def run(self):
        global current_line

        with open(self.src_file_name, mode='r', encoding='utf-8') as src:

            for exp in src.readlines():
                current_line += 1

                obj = Token(exp)

                TranslateToPython(obj.types, obj.values)


        try:
            exec(py_code, globals(), globals())


        except:
            error = format_exc().split('File "<string>", ')[-1]
            print(f'Exception in {error}\n', '------'*10)

            print('"' + "There ain't no mistaking, is true love we are making~" + '"')



Main()