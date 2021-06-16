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



KW_print         = 'i_just_wanna_tell_u_how_im_feeling:'
KW_if            = 'and_if_u_ask_me_how_im_feeling'

KW_let           = 'give_u_up'
KW_local_let     = 'u_wont_get_this_from_any_other_guy'
KW_def           = 'def'
KW_main          = 'take_me_to_ur_heart'
KW_end_main      = 'never_let_me_go'
KW_end           = 'say_good_bye'
KW_try           = 'i_dont_know_if_i_can_make_it'
KW_except        = 'even_if_im_broken_on_the_inside'
KW_import        = 'find_u'

KW_continue      = 'wanna_stay_inside_my_dream'
KW_break         = 'desert_u'
KW_loop          = 'together_forever_we_two'


KW_call_function = 'i_hear_ur_voice_calling:'



keywords = {
    KW_print,
    KW_if,
    KW_local_let,
    KW_let,
    KW_def,
    KW_main,
    KW_end_main,
    KW_end,
    KW_try,
    KW_except,
    KW_import,
    KW_continue,
    KW_break,
    KW_loop,
    KW_call_function
}



TT_keyword = 'KEYWORDS'

TT_arithmetic_operator = 'OPERATORS-Arithmetic'
TT_relational_operator = 'OPERATORS-Relational'
TT_assignment_operator = 'OPERATORS-Assignment'

TT_none                = 'VALUE-None'
TT_int                 = 'VALUE-Int'
TT_float               = 'VALUE-Float'
TT_bool                = 'VALUE-Bool'
TT_char                = 'VALUE-Char'
TT_string              = 'VALUE-String'
TT_list                = 'VALUE-List'
TT_hashmap             = 'VALUE-Hashmap'

TT_variable            = 'VARIABLE'
TT_function            = 'FUNCTION'
TT_p_variable          = 'P_VARIABLE'
TT_p_function          = 'P_FUNCTION'


# Set and start a timer
start = time()


digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}


seperator = {
    '(', ')', ',', '\n', '~', '=', ' ', '+', '-', '*', '/', '%', '^'
}

OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_assignment = {'='}


variables = []

indent_count = 0
current_line = 0


py_code = ''


def join(l):
    result = ''
    for i in l: result += f'{str(i)} '
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

            if char == '"': self.quote_count += 1

            if char == '#': break

            if char in seperator and self.quote_count % 2 == 0:

                if self.current_token != ' ' and self.current_token != '\n':
                    self.tokens.append(self.current_token)
                if char != ' ' and char != '\n':
                    self.tokens.append(char)

                self.current_token = ''

            else: self.current_token += char



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

        # If the token is a key word
        if self.tokens[i] in keywords:
            add_to_parser(TT_keyword)


    # Operators
        # Arithmetic Operators
        elif self.tokens[i] in OP_arithmetic:
            add_to_parser(TT_arithmetic_operator)

        # Relational Operator
        elif self.tokens[i] == 'is':
            self.types.append(TT_relational_operator)
            self.values.append('==')

        # Assignment Operator
        elif self.tokens[i] in OP_assignment:
            add_to_parser(TT_assignment_operator)


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


        # Call function
        elif self.tokens[i - 1] == KW_call_function:
            add_to_parser(TT_p_function)


        # Others and possible variables
        elif self.tokens[i] in variables:
            add_to_parser(TT_variable)


        else:
            exit(f'Exception in line {current_line}: [{self.tokens[i]}]')


####################################################################################
'Translate To Python'
####################################################################################

class TranslateToPython:
    def __init__(self, types, values):

        global indent_count

        self.types = types
        self.values = values

        if (self.types) and self.types[0] == TT_keyword:
            kw = self.values[0]


            if kw == KW_print:
                # print EXP

                exp = join(self.values[1: len(self.values)])
                self.write(f'print({exp})\n')


            if kw == KW_let:
                # IDENTIFIER = VALUE

                exp = join(self.values[1: len(self.values)])
                self.write(f'{exp}\n')


            if kw == KW_if:
                # IF CONDITION:

                exp = join(self.values[1: len(self.values)])
                self.write(f'if {exp}:\n')

                indent_count += 1


            if kw == KW_loop:
                self.write('while True:\n')

                indent_count += 1


            if kw == KW_break:
                self.write('break\n')


            if kw == KW_end:
                indent_count -= 1


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
            if current_arg == '-sing': pass

            if current_arg == '-s': self.src_file_name = argv[i + 1]

            if current_arg == '-time': self.show_time = True

            if current_arg == '-mp3': self.is_mp3 = True


        self.execute_src()if exists(self.src_file_name)else print(f"File [{self.src_file_name}] doesn't exist...")


    def execute_src(self):

        global current_line

        with open(self.src_file_name, mode='r', encoding='utf-8') as src:

            for exp in src.readlines():
                current_line += 1

                TranslateToPython(Token(exp).types, Token(exp).values)


        try:
            exec(py_code)

        except Exception as error:
            print(f'Exception: [{error}]')


        if self.show_time:
            print(f'Execution Time: [{time() - start}] sec.')



if __name__ == '__main__':
    Main()