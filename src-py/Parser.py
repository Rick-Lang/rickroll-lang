from Keywords import *
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

    def endless_loop_node(Node: list, child_stmts):
        """
            endless_loop_node
                   |
               child_stmts
        """
        Node.append(["endless_loop_node", child_stmts])

    def func_node(Node:list, func_name, params, child_stmts):
        """
                    func_node
                 /      |      \
            func_name, params, child_stmts
        """
        Node.append(["func_node", func_name, params, child_stmts])

    def list_node(Node:list, items):
        """

        """

    def call_func(Node:list, func_name, func_params):
        """
                call_func_node
                /           \
            func_name   func_params
        """
        Node.append(["call_func_node", func_name, func_params])

class Parser(AST):
    def __init__(self, tokens: list[list[str]]):
        self.tokens = tokens
        self.nodes = []

        self.pos = 0
        self.stmt: Final = []

        while self.pos < len(self.tokens):
            self.parse()
            self.pos += 1

    def match(self, kw: str):
        # explanation at helpers.py
        return True if self.tokens[self.pos][0] == kw else False

    def parse(self):
        self.stmt = self.tokens[self.pos]
        if self.match(KW.MAIN.value):
            child_stmts = []
            indent_count = 1
            while indent_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    indent_count += 1
                elif self.tokens[self.pos][0] in KW.END.value:
                    indent_count -= 1
                child_stmts.append(self.tokens[self.pos])
            
            AST.func_node(self.nodes, "main", None, Parser(child_stmts).nodes)
        elif self.match(KW.DEF.value):
            func_name = self.stmt[1]
            params = [i for i in self.stmt[2:]]
            child_stmts = []
            indent_count = 1
            while indent_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    indent_count += 1
                elif self.tokens[self.pos][0] in KW.END.value:
                    indent_count -= 1
                child_stmts.append(self.tokens[self.pos])

            AST.func_node(self.nodes, func_name, params, Parser(child_stmts).nodes)
        elif self.match(KW.PRINT.value):
            AST.print_node(self.nodes, self.stmt[1:])

        elif self.match(KW.LET.value):
            AST.let_node(self.nodes, self.stmt[1], self.stmt[3:])

        elif self.match(KW.IF.value):
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

            AST.if_node(self.nodes, cond, Parser(child_stmts).nodes)

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

            AST.while_node(self.nodes, cond, Parser(child_stmts).nodes)

        elif self.match(KW.ENDLESS_LOOP.value):
            child_stmts = []
            indent_count = 1
            while indent_count != 0:
                self.pos += 1
                if self.tokens[self.pos][0] in INDENT_KW:
                    indent_count += 1
                elif self.tokens[self.pos][0] == KW.END.value:
                    indent_count -= 1

                child_stmts.append(self.tokens[self.pos])

            AST.endless_loop_node(self.nodes, Parser(child_stmts).nodes)

        elif self.match(KW.END.value):
            pass

        else:
            # Call function
            AST.call_func(self.nodes, self.tokens[self.pos][0], self.tokens[self.pos][1:])
