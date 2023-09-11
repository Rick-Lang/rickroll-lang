from typing import Final # explanation at Lexer.py

from sys import stdout
from time import time

from Keywords import *
from Lexer import lexicalize
from Parser import Parser, AST
from helpers import filter_str, precedence, starts_ends

start: Final = time()


def apply_op(a: int | str, b: int | str, op: str) -> int | str: # binary operation
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    # if op == '[': return 
    return 'True' if \
        op == '==' and a == b or op == KW.IS_NOT_OP.value and a != b \
        or op == '>' and a > b or op == '<' and a < b \
        or op == '>=' and a >= b or op == '<=' and a <= b \
    else 'False'

def apply_u_op(a: int | str, op: str): # unary operation
    if op == 'len': return len(a)
    return None

def evaluate(tokens: str):
    if len(tokens) == 1 and starts_ends(tokens[0], '"'):
        return filter_str(tokens[0])

    values: Final[list[int | str]] = []
    ops: Final[list[str]] = []

    i = 0
    while i < len(tokens):
        if not tokens[i]: return

        if tokens[i] == ' ':
            i += 1

        elif tokens[i] == '(':
            ops.append(tokens[i])

        elif starts_ends(tokens[i], '"'):
            values.append(filter_str(tokens[i]))

        elif tokens[i].isdigit():
            values.append(int(tokens[i]))

        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.pop()

        elif tokens[i] == '[':
            lst = ''
            while i < len(tokens):
                lst += tokens[i]
                i += 1

            values.append(lst)

        elif tokens[i] in OPERATORS:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.append(tokens[i])

        elif tokens[i] in OP_BUILT_IN_FUNCTIONS:
            expr = tokens[i + 2:tokens.index(")")] # from `(` to `)`
            if len(expr) == 1:
                values.append(apply_u_op(tokens[i], expr[0]))
            elif len(expr > 1):
                values.append(apply_u_op(tokens[i], evaluate(expr)))

        else: # Matched with variable

            var_value = str(variables[tokens[i]])
            values.append(int(var_value) if var_value.isdigit() else var_value)

        i += 1

    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_op(val1, val2, op))

    return values[-1]

variables: Final[dict[str, int | str | None]] = {}

class Interpreter:
    def __init__(self):
        self.idx = 0

    def interpret(self, nodes: list | str):
        for node in nodes:
            self.idx += 1
            if node[0] == "func_node":
                if node[1] == "main": # Main function
                    self.interpret(node[3])

            elif node[0] == "print_node":
                stdout.write(evaluate(node[1]))

            elif node[0] == "let_node":
                variables.update({node[1]: evaluate(node[2])})

            elif node[0] == "if_node":
                if evaluate(node[1]) == 'True':
                    self.interpret(node[2])

            elif node[0] == "while_node":
                while evaluate(node[1]) == 'True':
                    self.interpret(node[2])

def run(src_file_name: str, debug=False):

    intpr = Interpreter()
    Node = []

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()

        if len(content) > 0:
            content[-1] += '\n'  # EOF handling

        tokens = [lexicalize(stmt) for stmt in content if lexicalize(stmt) != ['']]

        if debug:
            stdout.write(f"tokens (LEXER): {tokens}\n\n")

        Node = Parser(tokens).nodes

        if debug:
            stdout.write("nodes (PARSER):\n")
            for i in range(len(Node)):
                stdout.write(f'{i} {Node[i]}\n')
                stdout.write('-' * 50)

        intpr.interpret(Node)
