from typing import Final
from sys import stdout

from Lexer import *
from helpers import join_list

# Keywords can execute outside main function
kw_exe_outside_main: Final = {KW.MAIN.value, KW.DEF.value, KW.IMPORT1.value}

variables: Final[list[str]] = []
functions: Final[list[str]] = []

current_line = 0

class Token:
    def __init__(self, tokens: list[str]):
        self.t_values: list[str] = []
        self.last_kw = ''

        for tok in tokens:
            if tok:
                self.__make_token(tok)

    def __make_token(self, tok: str):
        global variables, functions

        TOK_TO_OP: Final = {
            KW.E_OP.value: '==',
            KW.IS_NOT_OP.value: '!=',
            KW.G_OP.value: '>',
            KW.L_OP.value: '<',
            KW.GOE_OP.value: '>=',
            KW.LOE_OP.value: '<=',
        }

        TOK_TO_FN: Final = {
            'length': 'len',
            'to_string': 'str',
            'to_int': 'int',
            'to_float': 'float'
        }

        if tok in keywords:
            self.t_values.append(TOK_TO_OP.get(tok, tok))
            self.last_kw = tok

        elif tok in OP_build_in_functions:
            if tok in TOK_TO_FN:
                self.t_values.append(TOK_TO_FN[tok])

        # Variables
        elif self.last_kw == KW.LET.value:
            variables.append(tok)
            self.t_values.append(tok)
        # Functions
        elif self.last_kw == KW.DEF.value:
            functions.append(tok)
            self.t_values.append(tok)
        else:
            self.t_values.append(tok)


class TranslateToPython:
    def __init__(self):
        # tokens
        self.values = []
        self.is_main = False
        self.is_function = False
        self.indent_count = 0
        self.py_code = ""    # Python source code, translated from RickRoll source code

    def translate(self, values: list[str]):
        self.values = values
        # if there is no code in the current line of code
        if not self.values:
            self.write("")
            return
        if not (self.values[0] in keywords or self.values[0] in functions):
            stdout.write(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')
            return

        if self.is_main or (self.is_main == False and self.values[0] in kw_exe_outside_main) or self.is_function:
            # Convert Rickroll code to Python
            self.convert(kw=self.values[0])

        else:
            stdout.write(
                f'Exception in line {current_line}: [{self.values[0]}] can not be executed outside the main method\n'
            )


    def convert(self, kw: str):

        if kw in functions:
            self.write(join_list(self.values))

        elif kw == KW.MAIN.value:
            self.write('if __name__ == "__main__":')

            self.is_main = True
            self.indent_count += 1

        elif self.indent_count == 0:
            self.is_main = False
            self.is_function = False

        elif kw == KW.PRINT.value:
            """
                print xpr
            """

            xpr = join_list(self.values[1:])
            self.write(f'print({xpr}, end="")')

        elif kw == KW.LET.value:
            """
                let id up xpr
            """

            id = join_list(self.values[self.values.index(KW.LET.value) + 1 : self.values.index(KW.ASSIGN.value)])
            xpr = join_list(self.values[self.values.index(KW.ASSIGN.value) + 1:])
            self.write(f'{id} = {xpr}')

        elif kw == KW.IF.value:
            """
                if `cond`
            """

            cond = join_list(self.values[1:])
            self.write(f'if {cond}:')
            self.indent_count += 1

        elif kw == KW.TRY.value:
            self.write('try:')
            self.indent_count += 1

        elif kw == KW.EXCEPT.value:
            self.write('except:')
            self.indent_count += 1

        elif kw == KW.ENDLESS_LOOP.value:
            self.write('while True:')
            self.indent_count += 1

        elif kw == KW.WHILE_LOOP.value:
            """
                while1 `cond`
            """

            cond = join_list(self.values[1:])
            self.write(f'while {cond}:')
            self.indent_count += 1

        elif kw == KW.BREAK.value:
            self.write('break')

        elif kw == KW.CONTINUE.value:
            self.write('continue')

        elif kw == KW.DEF.value:
            """
                def `id` ARGS
            """
            id = self.values[1]
            ARGS: Final = join_list(self.values[2:])

            self.write(f'def {id}({ARGS}):')

            self.is_function = True
            self.indent_count += 1

        elif kw == KW.RETURN1.value:
            """
                return1 `xpr` return2
            """
            xpr = join_list(self.values[1:])
            self.write(f'return {xpr}')

        elif kw == KW.END.value:
            self.write('pass')
            self.indent_count -= 1

        elif kw == KW.IMPORT1.value:
            """
                import1 lib_name import2
            """
            self.write(f'import {self.values[1]}')

        elif kw == KW.PY.value:
            self.write(join_list(self.values[1:]))


    def write(self, stmt: str):
        self.py_code += f"{'  ' * self.indent_count + stmt}\n"


def run_in_py(src_file_name: str):
    global current_line

    transpiler = TranslateToPython()

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        if len(content) > 0:
            content[-1] += '\n'

        for statement in content:  # "statement" is a line of code the in source code
            current_line += 1

            token = Token(lexicalize(statement))
            transpiler.translate(values=token.t_values)

    return transpiler.py_code
