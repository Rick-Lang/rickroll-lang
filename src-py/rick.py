from sys import argv
from time import time
from os.path import exists


"""
Programming by writing code:   rick -s [File_Name]
Sing code:  rick -sing [MP3_Name] [File_Name]

Options:
-time : Show execution time of your code
-mp3 : Generate a mp3 audio file from your source code

"""


KW_print  = 'i_just_wanna_tell_u_how_im_feeling'
KW_if     = 'and_if_u_ask_me_how_im_feeling'

KW_let    = 'give_u_up'
KW_def    = 'def'
KW_main   = 'take_me_to_ur_heart'
KW_end    = 'say_good_bye'

KW_break  = 'desert_u'
KW_loop   = 'together_forever_we_two'



keywords = {
    KW_print,
    KW_if,
    KW_let,
    KW_def,
    KW_main,
    KW_end,
    KW_break,
    KW_loop,
}


TT_keyword = 'KEYWORDS'

TT_operator            = 'OPERATORS'
# TT_arithmetic_operator = 'OPERATORS-Arithmetic'
# TT_relational_operator = 'OPERATORS-Relational'
# TT_assignment_operator = 'OPERATORS-Assignment'
# TT_other_operator      = 'OPERATORS-Other'

TT_none                = 'VALUE-None'
TT_int                 = 'VALUE-Int'
TT_float               = 'VALUE-Float'
TT_bool                = 'VALUE-Bool'
TT_char                = 'VALUE-Char'
TT_string              = 'VALUE-String'

TT_variable            = 'VARIABLE'
TT_function            = 'FUNCTION'
TT_p_variable          = 'P_VARIABLE'
TT_p_function          = 'P_FUNCTION'


# Set and start a timer
start = time()


digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}


seperator = {
    '(', ')', '[', ']', ',', '\n', ' ', '+', '-', '*', '/', '%', '^'
}


OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_relational = {'is', 'is_not', 'is_greater_than', 'is_less_than'}
OP_assignment = {'='}
OP_other      = {'[', ']', '(', ')', '{', '}', ','}

OP_type_conversion = {'ToString', 'ToInt', 'ToFloat'}


variables = []


indent_count = 0
current_line = 0


py_code = ''


def join(l):
    result = ''
    for i in l: result += f'{i} '
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


        # If the token is a key word
        if self.tokens[i] in keywords:
            add_to_parser(TT_keyword)


    # Operators
        # Arithmetic Operators
        elif self.tokens[i] in OP_arithmetic or self.tokens[i] in OP_assignment or self.tokens[i] in OP_other:
            add_to_parser(TT_operator)

        # Relational Operator
        elif self.tokens[i] in OP_relational:
            if self.tokens[i] == 'is':
                add_operator('==')

            if self.tokens[i] == 'is_not':
                add_operator('!=')


            if self.tokens[i] == 'is_greater_than':
                add_operator('<=')


            if self.tokens[i] == 'is_less_than':
                add_operator('>=')


        elif self.tokens[i] in OP_type_conversion:
            if self.tokens[i] == 'ToString':
                add_operator('str')

            if self.tokens[i] == 'ToInt':
                add_operator('int')

            if self.tokens[i] == 'ToFloat':
                add_operator('float')



    # Value
        # Int
        elif self.is_digit(self.tokens[i]) == 0:
            add_to_parser(TT_int)

        # Float
        elif self.is_digit(self.tokens[i]) == 1:
            add_to_parser(TT_float)

        # Bool
        elif self.tokens[i] == 'True' or self.tokens[i] == 'False':
            add_to_parser(TT_bool)

        # String
        elif self.tokens[i][0] == '"' and self.tokens[i][-1] == '"':
            add_to_parser(TT_string)


    # Others
        # Variables
        elif self.tokens[i - 1] == KW_let:
            add_to_parser(TT_variable)
            variables.append(self.tokens[i])


        # Function
        elif self.tokens[i - 1] == KW_def:
            add_to_parser(TT_function)


        # Others and possible variables
        elif self.tokens[i] in variables:
            add_to_parser(TT_variable)


        else:
            exit(f'<Exception in line {current_line}: "{self.tokens[i]}">')


####################################################################################
'Translate To Python'
####################################################################################

class TranslateToPython:
    def __init__(self, types, values):

        global indent_count

        self.types = types
        self.values = values

        if not self.types:
            self.write('\n')


        if (self.types) and self.types[0] == TT_keyword:
            kw = self.values[0]

            if kw == KW_print:
                # print EXP

                exp = join(self.values[1: len(self.values)])
                self.write(f'print({exp})\n')


            elif kw == KW_let:
                # IDENTIFIER = VALUE

                exp = join(self.values[1: len(self.values)])
                self.write(f'{exp}\n')


            elif kw == KW_if:
                # IF CONDITION:

                exp = join(self.values[1: len(self.values)])
                self.write(f'if {exp}:\n')

                indent_count += 1


            elif kw == KW_loop:
                self.write('while True:\n')

                indent_count += 1


            elif kw == KW_break:
                self.write('break\n')


            elif kw == KW_end:
                indent_count -= 1


            else:
                self.write('\n')


    def write(self, stmt):
        global py_code
        py_code += "\t" * indent_count + stmt



####################################################################################
'Main'
####################################################################################

class Main:
    def __init__(self):
        self.src_file_name = ''
        self.show_time = False


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            # Sing to write code
            if current_arg == '-s':
                self.src_file_name = argv[i + 1]

            if current_arg == '-time':
                self.show_time = True
                

        if exists(self.src_file_name):
            self.run()
        else:
            exit(f"File [{self.src_file_name}] doesn't exist...")


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
            exec(py_code)

        except Exception as error:
            print(f'<Exception: [{error}]>')


Main()