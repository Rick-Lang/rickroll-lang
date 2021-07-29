from time import time
from os.path import exists
from sys import argv, stdout

from PublicVariables import *

# Help message
rick_help = """
Programming by writing code:   rickroll -s [File_Name]
Generate an audio: rickroll -r [File_Name] -audio [Audio_Name]
Sing code:  rickroll -sing [Audio_Name] [File_Name]

Other Options:
--time:      Show execution time of your code
--help/--h:  Help
"""

# Token types
TT_keyword             = 'KEYWORDS'
TT_identifier          = 'IDENTIFIER'
TT_arithmetic_operator = 'OPERATORS-ARITHMETIC'
TT_assignment_operator = 'OPERATORS-ASSIGNMENT'
TT_relational_operator = 'OPERATORS-RELATIONAL'
TT_logical_operator    = 'OPERATORS-LOGICAL'
TT_other_operator      = 'OPERATORS-OTHER'

TT_int                 = 'VALUE-INT'
TT_float               = 'VALUE-FLOAT'
TT_bool                = 'VALUE-Bool'
TT_char                = 'VALUE-Char'
TT_string              = 'VALUE-String'

start = time()
current_line = 0

# For definining variables (Relevant: Interpreter, KW_let)
variables = {}


class Lexer:
    def __init__(self, statement):
        self.statement = statement

        self.tokens = []
        self.types = []       # Token type

        self.tokenize(self.statement)


    def tokenize(self, statement):
        current_token = ''
        quote_count = 0

        for char in statement:

            if char == '"': quote_count += 1
            if char == '#': break
            if char in ignore_tokens: continue

            if char in separators and quote_count % 2 == 0:

                if current_token != ' ' and current_token != '\n':
                    self.make_token(current_token)
                if char != ' ' and char != '\n':
                    self.make_token(char)

                current_token = ''
            else: current_token += char

    def make_token(self, t):

        def typeof(string):
            if string.count('"') == 2: return 'string'
            else:
                count = 0
                for i in string:
                    if i in digits: count += 1

                if len(string) == count:
                    if string.count('.') == 1: return 'float'
                    if string.count('.') == 0: return 'int'

        if t:
            self.tokens.append(t)
            if t in keywords:
                self.types.append(TT_keyword)
            elif t in OP_arithmetic:
                self.types.append(TT_arithmetic_operator)
            elif t in OP_assignment:
                self.types.append(TT_assignment_operator)
            elif t in OP_relational:
                self.types.append(TT_relational_operator)
            elif t in OP_logical:
                self.types.append(TT_logical_operator)
            elif t in OP_other:
                self.types.append(TT_other_operator)
            elif typeof(t) == 'int':
                self.types.append(TT_int)
            elif typeof(t) == 'float':
                self.types.append(TT_float)
            elif typeof(t) == 'string':
                self.types.append(TT_string)
            else:
                self.types.append(TT_identifier)


class Interpreter:
    def __init__(self, types, tokens):
        self.types = types
        self.tokens = tokens
        self.error_exp = ''    # expression; used to return errors;

        if self.types[0] == TT_keyword:
            self.run_code(kw=self.tokens[0])

    def evaluate(self, types=[], tokens=[]):
        for i in range(len(types)):
            if types[i] == TT_identifier:
                tokens[i] = variables[tokens[i]]

            if types[i] == TT_relational_operator:
                if tokens[i] == 'is_greater_than':
                    tokens[i] = '>'
                if tokens[i] == 'is_less_than':
                    tokens[i] = '<'
                if tokens[i] == 'is':
                    tokens[i] = '=='
                if tokens[i] == 'is_not':
                    tokens[i] = '!='

        return eval(join_list(tokens))


    def run_code(self, kw):
        if kw == KW_print:
            """
            PRINT EXPR
            """
            EXPR = self.evaluate(self.types[1:], self.tokens[1:])
            stdout.write(str(EXPR))

        elif kw == KW_if:
            """
            IF CONDI
            """
            CONDI = self.evaluate(self.types[1:], self.tokens[1:])
            if CONDI:
                stdout.write("Valid If Statement")

        elif kw == KW_endless_loop:
            pass

        elif kw == KW_while_loop:
            """
            WHILE CONDI
            """
            CONDI = self.evaluate(self.types[1:], self.tokens[1:])

        elif kw == KW_let:
            """
            LET ID = EXPR
            """
            ID = self.tokens[self.tokens.index(KW_let) + 1]
            EXPR = join_list(self.tokens[self.tokens.index('=') + 1:])
            variables.update({ID: EXPR})

        elif kw == KW_end:
            pass


def run_in_interpreter(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for i in range(len(content)):
            current_line += 1
            obj = Lexer(statement=content[i])    # "statement" is a line of code the in source code

            # Run code
            # try:
            if obj.tokens:
                Interpreter(types=obj.types, tokens=obj.tokens)

            # except Exception as e:
            #     stdout.write(f'Exception in line {current_line}: {e}\n')