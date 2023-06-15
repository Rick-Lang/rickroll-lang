from typing import Final # explanation at Lexer.py

from sys import stdout
from time import time

from Keywords import *
from Lexer import lexicalize
from Parser import Parser, AST
from helpers import filter_str, precedence, starts_ends

start: Final = time()


def applyOp(a: int | str, b: int | str, op: str) -> int | str:
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    return 'True' if \
        op==KW.E_OP.value and a==b or op==KW.IS_NOT_OP.value and a!=b \
        or op==KW.G_OP.value and a>b or op==KW.L_OP.value and a<b \
        or op==KW.GOE_OP.value and a>=b or op==KW.LOE_OP.value and a<=b \
    else 'False'

def evaluate(tokens: str):
    if len(tokens) == 1 and starts_ends(tokens[0], '"'):
        return filter_str(tokens[0])

    values: Final[list[int | str]] = []
    ops: Final[list[str]] = []

    for i in range(len(tokens)):
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
                values.append(applyOp(val1, val2, op))
            ops.pop()
        elif tokens[i] in OPERATORS:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))
            ops.append(tokens[i])
        else:
            var_value = str(variables[tokens[i]])
            values.append(int(var_value) if var_value.isdigit() else var_value)

        i += 1

    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(applyOp(val1, val2, op))
    return values[-1]

variables: Final[dict[str, int | str | None]] = {}

class Interpreter:
    def __init__(self):
        self.idx = 0

    def interpret(self, nodes: list | str):
        for node in nodes:
            self.idx += 1

            if node[0] == "print_node":
                stdout.write(evaluate(node[1]))

            elif node[0] == "let_node":
                variables.update({node[1]:evaluate(node[2])})

            elif node[0] == "if_node":
                if evaluate(node[1]) == 'True':
                    self.interpret(node[2])

            elif node[0] == "while_node":
                while evaluate(node[1]) == 'True':
                    self.interpret(node[2])


def run_in_interpreter(src_file_name: str):
    intpr = Interpreter()
    Node = []

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        if len(content) > 0:
            content[-1] += '\n'
        tokens = [lexicalize(stmt) for stmt in content if lexicalize(stmt) != []]
        print(tokens)
        Node = Parser(tokens).nodes
        # print("parser:")
        # for i in Node:
        #     print('-----')
        #     print(i)

        intpr.interpret(Node)
