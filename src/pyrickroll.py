import sys
import Lexer

from typing import Final
from Keywords import KW, KEYWORDS
from helpers import join_list


variables: Final[list[str]] = []
functions: Final[list[str]] = []

current_line = 0

class TranslateToPython:
    def __init__(self):
        # tokens
        self.values: list[str] = []
        # self.is_main = False
        self.indent_count = 0
        self.py_code = ""    # Python code translated from RickRoll

    def translate(self, values: list[str]):
        self.values = values
        # if there is no code in the current line of code
        if not self.values:
            return

        if self.values[0] and self.values[0] not in KEYWORDS:
            sys.stdout.write(f"Rickroll exception in line {current_line}: '{self.values[0]}' is invalid\n")

        # Convert Rickroll code to Python
        self.convert(kw=self.values[0])


    def convert(self, kw: str):

        if kw in functions:
            self.write(join_list(self.values))

        elif kw == KW.MAIN.value:
            self.write('if __name__ == "__main__":')

            # self.is_main = True
            self.indent_count += 1

        elif kw == KW.PRINT.value:
            """
                print expr
            """

            expr = join_list(self.values[1:])
            self.write(f'print({expr}, end="")')

        elif kw == KW.LET.value:
            """
                let id up expr
            """

            id = join_list(self.values[self.values.index(KW.LET.value) + 1 : self.values.index(KW.ASSIGN.value)])
            expr = join_list(self.values[self.values.index(KW.ASSIGN.value) + 1:])
            self.write(f'{id} = {expr}')

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
            ARGS = join_list(self.values[2:])

            self.write(f'def {id}({ARGS}):')

            self.indent_count += 1

        elif kw == KW.CALL.value:
            """
                call FUNC
            """
            self.write(f'{join_list(self.values[1:])}')

        elif kw == KW.RETURN1.value:
            """
                return1 `expr` return2
            """
            expr = join_list(self.values[1:-2])
            self.write(f'return {expr}')

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

        else:
            self.write(join_list(self.values))


    def write(self, stmt: str):
        self.py_code += f"{'    ' * self.indent_count + stmt}\n"


def run(file_name: str):

    global current_line

    transpiler = TranslateToPython()

    with open(file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        if len(content) > 0:
            content[-1] += '\n'

        for statement in content:  # "statement" is a line of code in the source code
            current_line += 1

            tokens = [value for kind, value in Lexer.tokenize(statement)]
            transpiler.translate(tokens)

    return transpiler.py_code
