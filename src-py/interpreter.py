from sys import stdout
from time import time

from Keywords import *
from Lexer import lexicalize
from helpers import filter_str, precedence, starts_ends

start = time()

class AST:
    def print_node(Node: list, args):
        """
            print_node
                |
               args
        """
        Node.append(["print_node", args])

    def let_node(Node: list, name, expr):
        """
              let_node
               /     \
             name  expr(value)
        """
        Node.append(["let_node", name, expr])

    def if_node(Node: list, cond, child_stmts):
        """
              if_node
                /  \
            cond  child_stmts
        """
        Node.append(["if_node", cond, child_stmts])

    def while_node(Node: list, cond, child_stmts):
        """
              while_node
               /     \
            cond    child_stmts
        """
        Node.append(["while_node", cond, child_stmts])


class Parser(AST):
    def __init__(self, tokens: list[list[str]], Node: list):
        self.Node = Node
        self.tokens = tokens

        self.pos = 0
        self.stmt = []

        while self.pos < len(self.tokens):
            self.parse()
            self.pos += 1

    def match(self, kw: str):
        return True if self.tokens[self.pos][0] == kw else False

    def parse(self):
        self.stmt = self.tokens[self.pos]
        if self.match(KW.PRINT.value):
            AST.print_node(self.Node, self.stmt[1:])

        elif self.match(KW.LET.value):
            AST.let_node(self.Node, self.stmt[1], self.stmt[3:])

        elif self.match(KW.IF.value):
            cond = self.stmt[1:]
            child_stmts = []
            if_count = 1
            while if_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    if_count += 1
                elif self.tokens[self.pos][0] == KW.END.value:
                    if_count -= 1

                child_stmts.append(self.tokens[self.pos])
            if_nodes = []
            Parser(tokens=child_stmts, Node=if_nodes)
            AST.if_node(self.Node, cond, if_nodes)

        elif self.match(KW.WHILE_LOOP.value):
            cond = self.stmt[1:]
            child_stmts = []
            indent_count = 1
            while indent_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    indent_count += 1
                elif self.tokens[self.pos][0] == KW.END.value:
                    indent_count -= 1

                child_stmts.append(self.tokens[self.pos])

            while_nodes = []
            Parser(tokens=child_stmts, Node=while_nodes)
            AST.while_node(self.Node, cond, while_nodes)

def applyOp(a, b, op: str):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    return 'True' if \
        op==KW.E_OP.value and a==b or op==KW.IS_NOT_OP.value and a!=b \
        or op==KW.G_OP.value and a>b or op==KW.L_OP.value and a<b \
        or op==KW.GOE_OP.value and a>=b or op==KW.LOE_OP.value and a<=b \
    else 'False'

def evaluate(tokens: list[str]):
    if len(tokens) == 1 and starts_ends(tokens[0], '"'):
        return filter_str(tokens[0])

    values = []
    ops: list[str] = []

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
        elif tokens[i] in operators:
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

variables = {}

class Interpreter:
    def __init__(self):
        self.idx = 0

    def interpret(self, nodes: list[list]):
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
    Node: list[list] = []

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        tokens = [lexicalize(stmt) for stmt in content if lexicalize(stmt) != []]
        Parser(tokens=tokens, Node=Node)

        intpr.interpret(Node)
