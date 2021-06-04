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
KW_end_main      = 'this_old_house_is_the_way_u_should_be'
KW_end_statement = 'say_good_bye'
KW_try           = 'i_dont_know_if_i_can_make_it'
KW_except        = 'even_if_im_broken_on_the_inside'
KW_import        = 'find_u'

KW_continue      = 'wanna_stay_inside_my_dream'
KW_break         = 'sometimes_i_feel_im_breaking_up'
KW_while         = "forever"
# KW_for           = ''

KW_call_function = 'i_hear_ur_voice_calling:'



keywords = {
    KW_print,
    KW_if,
    KW_local_let,
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
    KW_while,
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
    '(', ')', ',', '\n', '~', '=', ' ', '+', '-', '*', '/', '%', '^'
}

OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_logical    = {'||', '&&'}
OP_assignment = {'='}
OP_other      = {'~'}


functions = set({})
variables = {}


is_main = False
if_count = 0

current_line = 0


last_if_statement_result = False


def join(l):
    result = ''
    for i in l: result += str(i)

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

            if char in identifiers and self.quote_count % 2 == 0:

                if self.current_token != ' ' and self.current_token != '\n':
                    self.tokens.append(self.current_token)
                if char != ' ' and char != '\n':
                    self.tokens.append(char)

                self.current_token = ''

            else: self.current_token += char


            if self.quote_count % 2 != 0:
                pass



    def is_digit(self, string = ''):
        count = 0
        for i in string:
            if i in digits:
                count += 1

        if len(string) == count:
            if string.count('.') == 0: return 'int'
            if string.count('.') == 1: return 'float'


    # Convert each token to 
    def convert_token(self, i=0):

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
            # add_to_parser(TT_relational_operator)
            self.types.append(TT_relational_operator)
            self.values.append('==')

        # Logical Operator
        elif self.tokens[i] in OP_logical:
            add_to_parser(TT_logical_operator)

        # Assignment Operator
        elif self.tokens[i] in OP_assignment:
            add_to_parser(TT_assignment_operator)

        # Other Operator
        elif self.tokens[i] in OP_other:
            add_to_parser(TT_other_operator)

    # Value
        # Int
        elif self.is_digit(self.tokens[i]) == 'int':
            add_to_parser(TT_int)

        # Float
        elif self.is_digit(self.tokens[i]) == 'float':
            add_to_parser(TT_float)

        # Bool
        elif self.tokens[i] == 'TrueLove':
            add_to_parser(TT_bool)

        elif self.tokens[i] == 'TrueLove':
            add_to_parser(TT_bool)

        # String
        elif self.tokens[i][0] == '"' and self.tokens[i][-1] == '"':
            add_to_parser(TT_string)


    # Others
        # Variables
        elif self.tokens[i - 1] == KW_let:
            add_to_parser(TT_variable)


        # Function
        elif self.tokens[i - 1] == KW_def:
            add_to_parser(TT_function)
            functions.add(self.tokens[i])


        # Call function
        elif self.tokens[i - 1] == KW_call_function:
            add_to_parser(TT_p_function)


        # Others and possible variables
        else:
            add_to_parser(TT_p_variable)



####################################################################################
'Execute Function'
####################################################################################


class ExecuteFunction:
    def __init__(self):
        pass


####################################################################################
'Keywords Methods'
####################################################################################
class KeywordMethods:

    def __init__(self, types=[], values=[]):
        self.types = types
        self.values = values



    def _PRINT(self):
        self.values.remove(self.values[0])
        print(eval(join(self.values)))



    def _IF(self):
        global last_if_statement_result
        last_if_statement_result = eval(join(self.values[1 : len(self.values)]))



####################################################################################
'Parser'
####################################################################################

class Parser:
    def __init__(self, types, values):

        self.types = types
        self.values = values
        self.true_if_statement = False

        self.KeyMd = KeywordMethods(self.types, self.values)

        for i in range(len(self.types)):
            self.pre_execute(i)


        if self.true_if_statement:
            self.execute_main(kw=self.values[0])


        print(f'{current_line} : {last_if_statement_result}')


    def pre_execute(self, i=0):
        def add_variable():
            if self.types[i] == TT_p_variable and self.values[i] in variables:
                self.values[i] = variables[self.values[i]]

            # Add variables
            if self.types[i] == TT_variable and self.types[1]:
                source = eval(join(self.values[i+2 : len(self.values)]))
                variables.update({self.values[i]:f'"{source}"'if self.types[i+2]==TT_string else source})
        global is_main
        global if_count

        add_variable()


        if self.values[i] == KW_main: is_main = True
        if self.values[i] == KW_end_main: is_main = False

        if is_main and self.types[i] == TT_keyword:

            if self.values[i] == KW_if: if_count += 1
            if self.values[i] == KW_end_statement: if_count -= 1

            if if_count == 0 or self.values[0] == KW_if and if_count == 1:
                self.true_if_statement = True

            # print(f'line {current_line}: [{if_count}] {self.true_if_statement}')


    def execute_main(self, kw):
        if kw == KW_print:
            self.KeyMd._PRINT()

        if kw == KW_if:
            self.KeyMd._IF()


####################################################################################
'Main'
####################################################################################

class Main:
    def __init__(self):
        self.file_name = ''
        self.is_mp3 = False
        self.by_sing = False
        self.show_time = False


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            # Sing to write code
            if current_arg == '-sing': pass

            if current_arg == '-s': self.file_name = argv[i + 1]

            if current_arg == '-time': self.show_time = True

            if current_arg == '-mp3': self.is_mp3 = True


        self.execute_src()if exists(self.file_name)else print(f"File [{self.file_name}] doesn't exist...")


    def execute_src(self):

        global current_line

        with open(self.file_name, mode='r') as src:

            for exp in src.readlines():
                current_line += 1

                final_token_types = Token(exp).types
                final_token_values = Token(exp).values


                Parser(final_token_types, final_token_values)


        if self.show_time:
            print(f'Execution Time: [{time() - start}] sec.')



if __name__ == '__main__':
    Main()