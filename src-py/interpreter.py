from Keywords import *
from Lexer import lexicalize
from time import time
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
    def __init__(self, tokens, Node):
        self.Node = Node
        self.tokens = tokens

        self.pos = 0
        self.stmt = []

        while self.pos < len(self.tokens):
            self.parse()
            self.pos += 1

    def match(self, kw):
        return True if self.tokens[self.pos][0] == kw else False

    def parse(self):
        self.stmt = self.tokens[self.pos]
        if self.match(KW_print):
            AST.print_node(self.Node, self.stmt[1:])

        elif self.match(KW_let):
            AST.let_node(self.Node, self.stmt[1], self.stmt[3:])

        elif self.match(KW_if):
            cond = self.stmt[1:]
            child_stmts = []
            if_count = 1
            while if_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    if_count += 1
                elif self.tokens[self.pos][0] == KW_end:
                    if_count -= 1

                child_stmts.append(self.tokens[self.pos])
            if_nodes = []
            Parser(tokens=child_stmts, Node=if_nodes)
            AST.if_node(self.Node, cond, if_nodes)

        elif self.match(KW_while_loop):
            cond = self.stmt[1:]
            child_stmts = []
            indent_count = 1
            while indent_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    indent_count += 1
                elif self.tokens[self.pos][0] == KW_end:
                    indent_count -= 1

                child_stmts.append(self.tokens[self.pos])

            while_nodes = []
            Parser(tokens=child_stmts, Node=while_nodes)
            AST.while_node(self.Node, cond, while_nodes)

def filter_str(a):
    return a[1:-1]

def precedence(op):
    if op in {'+', '-'}: return 1
    if op in {'*', '/'}: return 2
    return 0

def applyOp(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    if op=='is'and a==b or op=='aint'and a!=b or op=='>'and a>b or op=='<'and a<b or op==">=" and a >= b or op=="<=" and a <= b:
        return 'True'
    return 'False'

def evaluate(tokens):
    if len(tokens) == 1:
        if tokens[0][0] == '"' and tokens[0][-1] == '"':
            return filter_str(tokens[0])

    values = []
    ops = []

    for i in range(len(tokens)):
        if not tokens[i]: return
        if tokens[i] == ' ':
            i += 1
        elif tokens[i] == '(':
            ops.append(tokens[i])
        elif tokens[i][0] == '"' and tokens[i][-1] == '"':
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

    def interpret(self, nodes):
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


def run_in_interpreter(src_file_name):
    intpr = Interpreter()
    Node = []

    with open(src_file_name, mode='r', encoding='utf-8') as src:
        content = src.readlines()
        content[-1] += '\n'
        tokens = [lexicalize(stmt) for stmt in content if lexicalize(stmt) != []]

        Parser(tokens=tokens, Node=Node)

        intpr.interpret(Node)

    print(f"\n{time() - start}")
