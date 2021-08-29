from time import time
from os.path import exists
from sys import argv, stdout

from PublicVariables import *
from Lexer import Lexer

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
TT_built_in_funcs      = 'OPERATORS-BUILT-IN-FUNCS'

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

in_loop = False
in_loop_stmts = []

while_condition = False

current_line = 0
# For definining variables (Relevant: Interpreter, KW_let)
variables = {}



test_types = ['KEYWORDS', 'VALUE-String']
test_tokens = ['i_just_wanna_tell_u_how_im_feeling', '"Hello\\n"']


# Determine variable types
def v_types(string):
    string = str(string)
    # Boolean
    if string == 'True' or string == 'False':
        return 'bool'
    # String
    if string[0] == '"' and string[-1] == '"':
        return 'string'
    # List
    if string[0] == '[' and string[-1] == ']':
        return 'list'
    # Determine the string is int or float
    count = 0
    for char in string:
        if char in digits:
            count += 1
    if count == len(string) and string.count('.') < 2:
        return 'number'

class Token:
    def __init__(self, raw_tokens):
        self.__raw_tokens = raw_tokens
        self.tokens = []      # Tokens
        self.types = []       # Token types

        for t in self.__raw_tokens:
            if t:
                self.make_token(t)

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
            elif t in OP_other:
                self.types.append(TT_other_operator)
            elif t in OP_build_in_functions:
                self.types.append(TT_built_in_funcs)
            elif typeof(t) == 'int':
                self.types.append(TT_int)
            elif typeof(t) == 'float':
                self.types.append(TT_float)
            elif typeof(t) == 'string':
                self.types.append(TT_string)
            else:
                self.types.append(TT_identifier)

class Eval:
    def __init__(self, tokens):
        self.__tokens = tokens
        self.values = []

        self.__evaluate(self.__tokens)

    def __precedence(self, op):
     
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == 'islessthan' or op == 'isgreaterthan' or op == 'is' or op == 'isnot':
            return 3
        return 0

    def __applyOp(self, a, b, op):
        
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b

    def __evaluate(self, tokens):
        ops = []

        for i in range(len(tokens)):
    
            if tokens[i] == '(':
                ops.append(tokens[i])
            
            elif tokens[i].isdigit():
                val = 0
                
                while (i < len(tokens) and tokens[i].isdigit()):
                
                    val = (val * 10) + int(tokens[i])
                    i += 1

                self.values.append(val)

            elif tokens[i][0] == '"' and tokens[i][-1] == '"':
                self.values.append(tokens[i][1: -1])


            elif tokens[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                
                    val2 = self.values.pop()
                    val1 = self.values.pop()
                    op = ops.pop()

                    self.values.append(self.__applyOp(val1, val2, op))
                
                ops.pop()

            elif tokens[i] == 'islessthan' or tokens[i] == 'isgreaterthan' or tokens[i] == 'is' or tokens[i] == 'isnot':
                ops.append(tokens[i])
                # val2 = self.values.pop()
                # val1 = self.values.pop()

                # self.values.append(val)


            else:
                while len(ops) != 0 and self.__precedence(ops[-1]) >= self.__precedence(tokens[i]):

                    val2 = self.values.pop()
                    val1 = self.values.pop()
                    op = ops.pop()

                    self.values.append(self.__applyOp(val1, val2, op))

                ops.append(tokens[i])


        for i in range(len(ops)):

            val2 = self.values.pop()
            val1 = self.values.pop()
            op = ops.pop()

            self.values.append(self.__applyOp(val1, val2, op))

        
    def __repr__(self):
        return f'{self.values[-1]}'


class Interpreter:
    def __init__(self, types, tokens):
        self.types = types
        self.tokens = tokens

        # If this line is executable or should be executed, then execute this line of code
        if self.types[0] == TT_keyword:
            self.run_code(kw=self.tokens[0])

    # Indentation, edits the two code levels
    def indent(self):
        global current_code_level, executing_code_level
        current_code_level += 1
        executing_code_level += 1


    # Get the value of an expression (EXPR)
    def eval_condition(self, types=[], tokens=[]):
        for i in range(len(types)):
            if types[i] == TT_identifier:
                tokens[i] = variables[tokens[i]]

            if types[i] == TT_keyword:
                if tokens[i] == 'isgreaterthan': tokens[i] = '>'
                if tokens[i] == 'islessthan': tokens[i] = '<'
                if tokens[i] == 'is': tokens[i] = '=='
                if tokens[i] == 'isnot': tokens[i] = '!='

        try:
            return eval(join_list(tokens))

        except SyntaxError:
            return eval(f'"{join_list(tokens)}"')


    def run_code(self, kw):
        global current_code_level, executing_code_level
        global in_loop, in_loop_stmts, while_condition


        """
            End statement
        """
        if kw == KW_end:
            
            run_loop = False

            if executing_code_level == current_code_level:
                executing_code_level -= 1

                # End a loop
                if in_loop:
                    in_loop = False
                    run_loop = True

            # the current code level go back 1
            current_code_level -= 1

            # Run the codes in loop
            if run_loop:
                while while_condition:
                    for stmt in in_loop_stmts:
                        Interpreter(stmt[0], stmt[1])


        # If the current code level should not execute, then return back (don't execute)
        if executing_code_level != current_code_level:
            return

        if in_loop:
            in_loop_stmts.append([self.types, self.tokens])
            return


        if kw == KW_main:
            self.indent()

        elif kw == KW_print:
            """
                PRINT EXPR
            """
            # EXPR = Evaluate(self.types[1:], self.tokens[1:])
            EXPR = str(Eval(self.tokens[1:]))
            for i in EXPR.split("\\n"):
                stdout.write(f'{i}\n')

        elif kw == KW_if:
            """
                IF CONDI
            """
            CONDI = self.eval_condition(types=self.types[1:], tokens=self.tokens[1:])
            # If the condition is true, execute the next code level (executing_code_level += 1)
            if CONDI:
                executing_code_level += 1

            current_code_level += 1

        elif kw == KW_endless_loop:
            in_loop = True
            while_condition = True
            self.indent()

        elif kw == KW_while_loop:
            """
                WHILE CONDI
            """
            # CONDI = Evaluate(self.types[1:], self.tokens[1:])
            CONDI = self.eval_condition(self.tokens[1:])
            while_condition = CONDI
            if CONDI:
                in_loop = True
                executing_code_level += 1
            current_code_level += 1

            # self.indent()

        elif kw == KW_let:
            """
                LET ID up EXPR
            """
            ID = self.tokens[self.tokens.index(KW_let) + 1]

            EXPR = str(Eval(tokens = self.tokens[self.tokens.index(KW_assign) + 1:]))
            variables.update({ID: EXPR})


def run_in_interpreter(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for i in range(len(content)):
            current_line += 1
            lexer = Lexer(stmt=content[i])    # "statement" is a line of code the in source code
            token = Token(raw_tokens=lexer.tokens)
            if token.tokens:
                try:
                    Interpreter(types=token.types, tokens=token.tokens)

                except Exception as e:
                    stdout.write(f'Exception in line {current_line}: {e}\n')
