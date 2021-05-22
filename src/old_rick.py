from sys import argv
from time import time

start = time()

"""
Processes:
(1) Open source file
(2) Split src code into expressions
(3) Tokenize each expression
(4) Lexicalize tokens
(5) Store variables
(6) Code priority
(7) Match keywords
"""

"""
Programming by writing code:   rick -s [File_Name]
Sing code:  rick -sing [MP3_Name] [File_Name]

Options:
-time : Show execution time of your code
-mp3 : Generate a mp3 audio file from your source code

"""





KW_PRINT         = 'i_just_wanna_tell_u_how_im_feeling:'
KW_IF            = 'and_if_u_ask_me_how_im_feeling:'
KW_CONST_LET     = 'never_gonna_let_u_down'
KW_LET           = 'let_u_down'
KW_DEF           = 'def'
KW_MAIN          = 'take_me_to_ur_heart'
KW_END           = 'this_old_house_is_the_way_u_should_be'
KW_END_STATEMENT = 'say_good_bye'
KW_TRY           = 'i_dont_know_if_i_can_make_it'
KW_EXCEPT        = 'even_if_im_broken_on_the_inside'
KW_IMPORT        = 'find_u'
KW_VOID          = ''

KW_CONTINUE      = 'wanna_stay_inside_my_dream'
KW_BREAK         = 'sometimes_i_feel_im_breaking_up'
KW_WHILE_TRUE    = "it's_the_dream_that_never_fades"
KW_FOR           = 'forever'

KW_CALL_FUNC     = 'i_hear_ur_voice_calling:'



keywords = {
    KW_PRINT,
    KW_IF,
    KW_CONST_LET,
    KW_LET,
    KW_DEF,
    KW_TRY,
    KW_EXCEPT,
    KW_IMPORT,
    KW_CONTINUE,
    KW_BREAK,
    KW_WHILE_TRUE,
    KW_FOR,
    KW_CALL_FUNC,
    KW_MAIN,
    KW_END
}


digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}


TT_STRING       = 'STRING'
TT_CHAR         = 'CHAR'
TT_BOOLEAN      = 'BOOLEAN'
TT_INT          = 'INT_NUM'
TT_FLOAT        = 'FLOAT_NUM'
TT_LIST         = 'LIST'
TT_SET          = 'SET'
TT_HASHMAP      = 'HASHMAP'
TT_FUNCTION     = 'FUNCTION'

TT_KEYWORD      = 'KEY_WORD'
TT_OPERATOR     = 'OPERATOR'
TT_VARIABLE     = 'VARIABLE'
TT_P_VARIABLE   = 'POSSIBLE_VAR'
TT_P_FUNC       = 'POSSIBLE_FUNCTION'



operators = {
    '(', ')', ',', '\n', '+', '-', '*', '/', '~', '=', ' '
}


functions = set({})
variables = {}


#############################################################################
'Tokenize'
#############################################################################


class Token:
    def __init__(self, exp):
        self.exp = exp
        self.current_token = ''
        self.tokens = []
        self.quote_count = 0

        self.tokenize()


    def tokenize(self):

        for char in self.exp:

            if char == '"': self.quote_count += 1

            if char in operators and self.quote_count % 2 == 0:

                self.tokens.append(self.current_token)
                if char != ' ' and char != '\n': self.tokens.append(char)

                self.current_token = ''


            elif char == '#': break


            else: self.current_token += char



#############################################################################
'Exception Class'
#############################################################################



class Exception:
    def __init__(self):
        pass




#############################################################################
'Lexer Class'
#############################################################################


class Lexer:
    def __init__(self, tokens):
        self.tokens = tokens

        # TOKEN_TYPE : VALUE
        self.parser = {}


        for i in range(len(self.tokens)):
            if self.tokens[i] != '':
                self.lexicalize(i)



    # Determine it is a float or int or something else
    def is_digit(self, string = ''):
        count = 0
        for i in string:
            if i in digits:
                count += 1

        if len(string) == count:
            if string.count('.') == 0: return 'int'
            if string.count('.') == 1: return 'float'



    def lexicalize(self, i):


        # If the token is a key word
        if self.tokens[i] in keywords:
            self.parser.update({TT_KEYWORD : self.tokens[i]})


        # String
        elif self.tokens[i][0] == '"' and self.tokens[i][-1] == '"':
            self.parser.update({TT_STRING : self.tokens[i]})


        # Operators
        elif self.tokens[i] in operators:
            self.parser.update({TT_OPERATOR : self.tokens[i]})


        # INT
        elif self.is_digit(self.tokens[i]) == 'int':
            self.parser.update({TT_INT : self.tokens[i]})


        # FLOAT
        elif self.is_digit(self.tokens[i]) == 'float':
            self.parser.update({TT_FLOAT : self.tokens[i]})


        # BOOLEAN
        elif self.tokens[i] == 'true':
            self.parser.update({TT_BOOLEAN : 'true'})

        elif self.tokens[i] == 'false':
            self.parser.update({TT_BOOLEAN : 'false'})


        # Variables
        elif self.tokens[i - 1] == KW_LET or self.tokens[i - 1] == KW_CONST_LET:
            self.parser.update({TT_VARIABLE : self.tokens[i]})


        # Function
        elif self.tokens[i - 1] == KW_DEF:
            self.parser.update({TT_FUNCTION : self.tokens[i]})
            functions.add(self.tokens[i])


        # Call function
        elif self.tokens[i - 1] == KW_CALL_FUNC:
            self.parser.update({TT_P_FUNC : self.tokens[i]})


        # Others and possible variables
        else:
            self.parser.update({TT_P_VARIABLE : self.tokens[i]})


#############################################################################
'Execute inner Functions'
#############################################################################
class Keywords:

    is_str = lambda string: True if string.count('"') >= 2 else False


    def _print(self, _input='', t_type=''):

        if t_type == TT_STRING: return _input[1:-1]

        elif t_type == TT_P_VARIABLE and _input in variables:
            return variables[_input][1:-1] if is_str(variables[_input]) else variables[_input]

        else:  return _input



    def get_expression_value(self, exp):
        pass



    def _if(self, words, types):
        """
        num is 10
        var1 - var2 is 10
        i_hear_ur_vioce_calling is_str var1 is false
        """
        checking_expression = {}
        result = ''

        for i in range(len(words[1:-1])):

            if words[i] == 'is':

                exp_value = self.get_expression_value(checking_expression)

                if exp_value == result:
                    pass

            else:
                checking_expression.update({types[i] : words[i]})


#############################################################################
'Interpreter'
#############################################################################
is_main = False


class Interpreter(Keywords):

    def __init__(self, parser={}):
        self.parser = parser
        self.add_var()
        self.interpret()


    def add_var(self):

        for i in range(len(self.parser.keys())):

            types = list(self.parser.keys())
            words = list(self.parser.values())


            if types[i] == TT_VARIABLE:
                if types[i + 1] != TT_OPERATOR:
                    variables.update({words[i] : 0})

                elif words[i + 1] == '=':
                    variables.update({words[i] : words[i + 2]})


    def interpret(self):
        global is_main

        for i in range(len(self.parser.keys())):

            types = list(self.parser.keys())
            words = list(self.parser.values())


            if is_main and types[i] == TT_KEYWORD:

                # Print
                if words[i] == KW_PRINT:
                    print(Keywords._print(self, words[i + 1], types[i + 1]))

                # If statement
                elif words[i] == KW_IF:
                    print(Keywords._if(self, words, types))


                else:
                    pass


            if words[i] == KW_MAIN: is_main = True
            if words[i] == KW_END: is_main = False



#############################################################################
'Get Expression Value'
#############################################################################
class ExpValue:
    def __init__(self):
        pass




#############################################################################
'Main'
#############################################################################


class Main:
    def __init__(self):
        self.file_name = ''
        self.is_mp3 = False
        self.show_time = False
        self.by_sing = False


        for i in range(len(argv)):

            current_arg = argv[i].lower()

            # Using sing method to write code
            if current_arg == '-sing':
                pass


            if current_arg == '-s':
                self.file_name = argv[i + 1]


            if current_arg == '-time':
                self.show_time = True


            if current_arg == '-mp3':
                self.is_mp3 = True


        self.execute_main()


    def execute_main(self):
        with open(self.file_name, mode='r') as src:

            for exp in src.readlines():

                Interpreter(Lexer(Token(exp).tokens).parser)


        if self.show_time:
            print(f'Execution Time: [{time() - start}] sec.')


try:
    Main()


except FileExistsError or FileNotFoundError:
    print(f'File [{argv[-1]}] does not exists...')
