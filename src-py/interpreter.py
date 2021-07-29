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

"""
Code level works as indentation in python
"""
# The current code level the interpreter is reading
current_code_level = 0
# The code level that the interpreter should execute or interpret
executing_code_level = 0

current_line = 0
# For definining variables (Relevant: Interpreter, KW_let)
variables = {}


class Lexer:
    def __init__(self, statement):
        self.statement = statement

        self.tokens = []      # Tokens
        self.types = []       # Token types

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

            count = 0
            for i in string:
                if i in digits: count += 1
            if count == len(string):
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

        # If this line is executable or should be executed, then execute this line of code
        if self.types[0] == TT_keyword:
            self.run_code(kw=self.tokens[0])

    # Indentation, edits the two code levels
    def indent(self):
        global current_code_level, executing_code_level
        current_code_level += 1
        executing_code_level += 1


    # Get the value of an expression (EXPR)
    def evaluate(self, types=[], tokens=[]):
        for i in range(len(types)):
            if types[i] == TT_identifier:
                tokens[i] = variables[tokens[i]]

            if types[i] == TT_relational_operator:
                if tokens[i] == 'is_greater_than': tokens[i] = '>'
                if tokens[i] == 'is_less_than': tokens[i] = '<'
                if tokens[i] == 'is': tokens[i] = '=='
                if tokens[i] == 'is_not': tokens[i] = '!='

        return eval(join_list(tokens))


    def run_code(self, kw):
        global current_code_level, executing_code_level

        """
            End statement, which 
        """
        if kw == KW_end:
            if executing_code_level == current_code_level:
                executing_code_level -= 1

            # the current code level go back 1
            current_code_level -= 1

        # If the current code level should not execute, then return back (don't execute)
        if executing_code_level != current_code_level:
            return

        if kw == KW_main:
            self.indent()

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
                executing_code_level += 1

            current_code_level += 1

        elif kw == KW_endless_loop:
            self.indent()

        elif kw == KW_while_loop:
            """
            WHILE CONDI
            """
            CONDI = self.evaluate(self.types[1:], self.tokens[1:])

            self.indent()

        elif kw == KW_let:
            """
            LET ID = EXPR
            """
            ID = self.tokens[self.tokens.index(KW_let) + 1]

            EXPR = self.evaluate(
                types=self.types[self.types.index(TT_assignment_operator) + 1:],
                tokens=self.tokens[self.types.index(TT_assignment_operator) + 1:]
            )
            variables.update({ID: EXPR})


def run_in_interpreter(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for i in range(len(content)):
            current_line += 1
            obj = Lexer(statement=content[i])    # "statement" is a line of code the in source code

            if obj.types:
            # try:
                Interpreter(types=obj.types, tokens=obj.tokens)

            # except Exception as e:
            #     stdout.write(f'Exception in line {current_line}: {e}\n')