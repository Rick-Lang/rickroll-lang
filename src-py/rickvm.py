from sys import stdout
"""
print: print EXPR
jmp: jmp LINE COND
var: var NAME VALUE
"""

def filter_str(a):
    return a[1:-1]

def precedence(op):
    if op in ['+', '-']: return 1
    if op in ['*', '/']: return 2
    return 0

def applyOp(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    if op=='=='and a==b or op=='!='and a!=b or op=='>'and a>b or op=='<'and a<b or op==">=" and a >= b or op=="<=" and a <= b:
        return 'True'
    return 'False'

def evaluate(tokens):
    if len(tokens) == 1:
        if tokens[0][0] == '"' and tokens[0][-1] == '"':
            return filter_str(tokens[0])
        return tokens[0]

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

        elif tokens[i] in OPERATORS:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))

            ops.append(tokens[i])

        else:
            var_value = variables[tokens[i]]
            values.append(int(var_value) if var_value.isdigit() else var_value)

        i += 1

    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(applyOp(val1, val2, op))
    return values[-1]


variables = {}
OPERATORS = {'+', '-', '*', '/', '==', '>', '<', '<=', '>=', '!='}

class RickVM(object):
    def __init__(self):
        self.stmts = []
        self.idx = 0

    def run_vm(self, stmts):
        self.stmts = stmts
        while self.idx < len(stmts):
            self.execute(self.stmts[self.idx])
            self.idx += 1

    def execute(self, stmt):
        if stmt[0] == "print":
            stdout.write(str(evaluate(stmt[1:])))
        elif stmt[0] == "jmp":
            if evaluate(stmt[2:]) == "True":
                self.execute(self.stmts[int(stmt[1])])
                self.idx = int(stmt[1])

        elif stmt[0] == "var":
            variables.update({stmt[1] : evaluate(stmt[2:])})

# idx = 0
#
# def execute(stmt):
#     global idx
#     if stmt[0] == "print":
#         stdout.write(str(evaluate(stmt[1:])))
#     elif stmt[0] == "jmp":
#         if evaluate(stmt[2:]) == "True":
#             execute(stmts[stmt[1]])
#             idx = stmt[1]
#
#     elif stmt[0] == "var":
#         variables.update({stmt[1] : evaluate(stmt[2:])})
#
# while idx < len(stmts):
#     execute(stmts[idx])
#     idx += 1
#
