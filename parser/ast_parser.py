import ast

class CodeParser(ast.NodeVisitor):
    def __init__(self):
        self.flow = []

    def visit_FunctionDef(self, node):
        self.flow.append(f"Function: {node.name}")
        self.generic_visit(node)

    def visit_If(self, node):
        condition = ast.unparse(node.test)
        self.flow.append(f"If: {condition}")
        self.generic_visit(node)

    def visit_For(self, node):
        loop = ast.unparse(node.target)
        self.flow.append(f"For loop: {loop}")
        self.generic_visit(node)

    def visit_While(self, node):
        condition = ast.unparse(node.test)
        self.flow.append(f"While: {condition}")
        self.generic_visit(node)

def parse_code(code):
    tree = ast.parse(code)
    parser = CodeParser()
    parser.visit(tree)
    return parser.flow
