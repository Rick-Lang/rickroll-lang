from PublicVariables import *
from Lexer import lexicalize

# Token types
TT_keyword        = 'KEYWORDS'
TT_identifier     = 'IDENTIFIER'
TT_operator       = 'OPERATOR'
TT_built_in_funcs = 'OPERATORS-BUILT-IN-FUNCS'
TT_function       = 'FUNCTION'

TT_int            = 'VALUE-INT'
TT_float          = 'VALUE-FLOAT'
TT_bool           = 'VALUE-Bool'
TT_char           = 'VALUE-Char'
TT_string         = 'VALUE-String'

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

# Functions
functions = dict({})
function_name = ""
function_content = []
in_function = False

# Determine variable types

def typeof(string):
    if string.count('"') == 2: return 'string'

    count = sum(i in digits for i in string)
    if count == len(string):
        if string.count('.') == 1: return 'float'
        if string.count('.') == 0: return 'int'


class Token:
    def __init__(self, raw_tokens):
        self.tokens = []      # Tokens
        self.types = []       # Token types
        self.__last_kw = ''

        for t in raw_tokens:
            if t:
                self.make_token(t)

    def make_token(self, t):
        self.tokens.append(t)
        if t in keywords:
            self.types.append(TT_keyword)
        elif t in operators:
            self.types.append(TT_operator)
        elif t in OP_build_in_functions:
            self.types.append(TT_built_in_funcs)
        elif typeof(t) == 'int':
            self.types.append(TT_int)
        elif typeof(t) == 'float':
            self.types.append(TT_float)
        elif typeof(t) == 'string':
            self.types.append(TT_string)
        elif self.__last_kw == KW_def1:
            self.types.append(TT_function)
            global function_name
            function_name = t
        else:
            self.types.append(TT_identifier)

        self.__last_kw = t

class Eval:
    def __init__(self, tokens, types=[]):
        self.__tokens = tokens
        self.__types = types
        self.values = []

        self.__evaluate(self.__tokens)

    def __precedence(self, op):

        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0

    def __applyOp(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b
        if op=='is'and a==b or op=='isnot'and a!=b or op=='isgreaterthan'and a>b or op=='islessthan'and a<b or op==KW_greater_or_equals_OP and a >= b:
            return 'TrueLove'
        else:
            return 'FalseLove'


    def __evaluate(self, tokens):
        ops = []

        for i in range(len(tokens)):

            if tokens[i] == '(':
                ops.append(tokens[i])

            elif tokens[i].isdigit():
                self.values.append(int(tokens[i]))

            elif self.__types[i] == TT_identifier:
                var_value = variables[tokens[i]]
                self.values.append(int(var_value) if var_value.isdigit() else var_value)

            elif tokens[i][0] == '"' and tokens[i][-1] == '"':
                self.values.append(tokens[i][1: -1])


            elif tokens[i] == ')':
                while ops and ops[-1] != '(':
                    val2 = self.values.pop()
                    val1 = self.values.pop()
                    op = ops.pop()

                    self.values.append(self.__applyOp(val1, val2, op))

                ops.pop()

            else:
                while ops and self.__precedence(ops[-1]) >= self.__precedence(
                    tokens[i]
                ):

                    val2 = self.values.pop()
                    val1 = self.values.pop()
                    op = ops.pop()

                    self.values.append(self.__applyOp(val1, val2, op))

                ops.append(tokens[i])


        while ops:
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

        if self.types[0] in [TT_keyword, TT_identifier]:
            self.run_code(kw=self.tokens[0])
        if self.types[0] == TT_identifier:
            self.run_func(func=self.tokens[0])

    # Indentation, edits the two code levels
    def indent(self):
        global current_code_level, executing_code_level
        current_code_level += 1
        executing_code_level += 1


    def run_code(self, kw):
        global current_code_level, executing_code_level
        global in_loop, in_loop_stmts, while_condition
        global in_function, function_content

        # End statement
        if kw == KW_end:

            run_loop = False

            # send back the executing_code_level
            if executing_code_level == current_code_level:
                executing_code_level -= 1

                if in_function:
                    functions.update({function_name:function_content})
                    in_function = False
                    function_content = []
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

        if in_function:
            function_content.append([self.types, self.tokens])
            return
        # If the current code level should not execute, then return back (don't execute)
        if executing_code_level != current_code_level:
            return

        if in_loop:
            in_loop_stmts.append([self.types, self.tokens])

        if kw == KW_main:
            self.indent()

        elif kw == KW_print:
            """
                PRINT EXPR
            """
            EXPR = str(Eval(self.tokens[1:], self.types[1:]))
            if '\\n' in EXPR:
                for i in EXPR.split("\\n")[:-1]:
                    stdout.write(f'{i}\n')
            else:
                stdout.write(EXPR)

        elif kw == KW_if:
            """
                IF CONDI
            """
            CONDI = str(Eval(types=self.types[1:], tokens=self.tokens[1:]))
            # If the condition is true, execute the next code level (executing_code_level += 1)
            if CONDI == 'TrueLove':
                executing_code_level += 1

            current_code_level += 1

        elif kw == KW_def1:
            in_function = True
 
        elif kw == KW_endless_loop:
            in_loop = True
            while_condition = True
            self.indent()

        elif kw == KW_break:
            in_loop = False
            while_condition = False
            in_loop_stmts.clear()
            return

        elif kw == KW_let:
            """
                LET ID up EXPR
            """
            ID = self.tokens[self.tokens.index(KW_let) + 1]

            EXPR = str(Eval(
                tokens=self.tokens[self.tokens.index(KW_assign)+1:],
                types=self.types[self.tokens.index(KW_assign)+1:]
            ))
            variables.update({ID: EXPR})
            
    def run_func(self, func):
        content = functions.get(func)
        for stmt in content:
            Interpreter(types=stmt[0], tokens=stmt[1])
            

def run_in_interpreter(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        for i in range(len(content)):
            current_line += 1
            tokens = lexicalize(stmt=content[i])    # "statement" is a line of code the in source code
            token = Token(raw_tokens=tokens)

            if token.tokens:
                try:
                    Interpreter(types=token.types, tokens=token.tokens)

                except Exception as e:
                    stdout.write(f'Exception in line {current_line}: {e}\n')
