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
KW_if            = 'and_if_u_ask_me_how_im_feeling:'
KW_const_let     = 'never_gonna_let_u_down'
KW_let           = 'give_u_up'
KW_def           = 'def'
KW_main          = 'take_me_to_ur_heart'
KW_end_main      = 'this_old_house_is_the_way_u_should_be'
KW_end_statement = 'say_good_bye'
KW_try           = 'i_dont_know_if_i_can_make_it'
KW_except        = 'even_if_im_broken_on_the_inside'
KW_import        = 'find_u'

KW_continue      = 'wanna_stay_inside_my_dream'
KW_break         = 'sometimes_i_feel_im_breaking_up'
KW_while_true    = "forever"
# KW_for           = ''

KW_call_function = 'i_hear_ur_voice_calling:'



keywords = {
    KW_print,
    KW_if,
    KW_const_let,
    KW_let,
    KW_def,
    KW_main,
    KW_end_main,
    KW_end_statement,
    KW_try,
    KW_except,
    KW_import,
    KW_continue,
    KW_break,
    KW_while_true,
    KW_call_function
}



TT_keyword = 'KEYWORDS'

TT_arithmetic_operator = 'OPERATORS-Arithmetic'
TT_relational_operator = 'OPERATORS-Relational'
TT_logical_operator    = 'OPERATORS-Logical'
TT_assignment_operator = 'OPERATORS-Assignment'
TT_other_operator      = 'OPERATORS-Other'

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


identifiers = {
    '(', ')', ',', '\n', '+', '-', '*', '/', '~', '=', '^', '%', ' '
}

OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_relational = {'is', 'not', 'greater', 'less', 'greater_equal', 'less_equal'}
OP_logical    = {'||', '&&'}
OP_assignment = {'=', '+=', '-=', '*=', '/=', '%=', '^='}
OP_other      = {'~'}


functions = set({})
variables = {}



####################################################################################
'Token Class'
####################################################################################
class Token:
    def __init__(self, exp):
        self.exp = exp
        self.parser = {}
        self.current_token = ''
        self.quote_count = 0
        self.tokens = []

        self.tokenize()

        for i in range(len(self.tokens)):
            if self.tokens[i] != '':
                self.convert_token(i)



    is_str = lambda string: True if string.count('"') >= 2 else False


    # Split statements to single word / token
    def tokenize(self):
        for char in self.exp:

            if char == '"': self.quote_count += 1

            if char in identifiers and self.quote_count % 2 == 0:

                self.tokens.append(self.current_token)
                if char != ' ' and char != '\n': self.tokens.append(char)

                self.current_token = ''


            elif char == '#': break


            else: self.current_token += char


    def is_digit(self, string = ''):
        count = 0
        for i in string:
            if i in digits:
                count += 1

        if len(string) == count:
            if string.count('.') == 0: return 'int'
            if string.count('.') == 1: return 'float'


    # Convert each token to 
    def convert_token(self, i):
        # If the token is a key word
        if self.tokens[i] in keywords:
            self.parser.update({TT_keyword : self.tokens[i]})


    # Operators
        # Arithmetic Operators
        elif self.tokens[i] in OP_arithmetic:
            self.parser.update({TT_arithmetic_operator : self.tokens[i]})

        # Relational Operator
        elif self.tokens[i] in OP_relational:
            self.parser.update({TT_relational_operator : self.tokens[i]})

        # Logical Operator
        elif self.tokens[i] in OP_logical:
            self.parser.update({TT_logical_operator : self.tokens[i]})

        # Assignment Operator
        elif self.tokens[i] in OP_assignment:
            self.parser.update({TT_assignment_operator : self.tokens[i]})

        # Other Operator
        elif self.tokens[i] in OP_other:
            self.parser.update({TT_other_operator : self.tokens[i]})

    # Value
        # Int
        elif self.is_digit(self.tokens[i]) == 'int':
            self.parser.update({TT_int : self.tokens[i]})

        # Float
        elif self.is_digit(self.tokens[i]) == 'float':
            self.parser.update({TT_float : self.tokens[i]})

        # Bool
        elif self.tokens[i] == 'true':
            self.parser.update({TT_bool : 'true'})

        elif self.tokens[i] == 'false':
            self.parser.update({TT_bool : 'false'})

        # String
        elif self.tokens[i][0] == '"' and self.tokens[i][-1] == '"':
            self.parser.update({TT_string : self.tokens[i]})


    # Others
        # Variables
        elif self.tokens[i - 1] == KW_let or self.tokens[i - 1] == KW_const_let:
            self.parser.update({TT_variable : self.tokens[i]})


        # Function
        elif self.tokens[i - 1] == KW_def:
            self.parser.update({TT_function : self.tokens[i]})
            functions.add(self.tokens[i])


        # Call function
        elif self.tokens[i - 1] == KW_call_function:
            self.parser.update({TT_p_function : self.tokens[i]})


        # Others and possible variables
        else:
            self.parser.update({TT_p_variable : self.tokens[i]})



####################################################################################
'Interpreter'
####################################################################################
class Interpreter:
    def __init__(self, parser):
        self.parser = parser


    # def execute_



####################################################################################
'Main'
####################################################################################
class Main:
    def __init__(self):
        self.file_name = ''
        # self.is_mp3 = False
        # # self.by_sing = False
        self.show_time = False
        self.current_line_count = 0


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            # Sing to write code
            # if current_arg == '-sing': pass


            if current_arg == '-s': self.file_name = argv[i + 1]


            if current_arg == '-time': self.show_time = True


            # if current_arg == '-mp3': self.is_mp3 = True


        self.execute_main()if exists(self.file_name)else print(f"File [{self.file_name}] doesn't exist...")


    def execute_main(self):

        with open(self.file_name, mode='r') as src:

            for exp in src.readlines():
                self.current_line_count += 1
                parser = Token(exp).parser
                print(parser)


        if self.show_time:
            print(f'Execution Time: [{time() - start}] sec.')



if __name__ == '__main__':
    Main()