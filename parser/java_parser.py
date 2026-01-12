import javalang
from parser.label_generator import HumanLabelGenerator


class JavaCodeParser:

    def __init__(self):
        self.labeler = HumanLabelGenerator()

    def parse(self, code):
        tree = javalang.parse.parse(code)
        steps = []

        for _, node in tree:

            if isinstance(node, javalang.tree.MethodDeclaration):
                steps.append({
                    "type": "process",
                    "label": self.labeler.method_label(node.name)
                })

            elif isinstance(node, javalang.tree.IfStatement):
                steps.append({
                    "type": "decision",
                    "label": self.labeler.if_label(node.condition),
                    "branches": self._block(),
                    "else": self._block()
                })

            elif isinstance(node, javalang.tree.TryStatement):
                steps.append({
                    "type": "try",
                    "label": self.labeler.try_label(),
                    "try": self._block(),
                    "catch": [{
                        "type": "exception",
                        "label": self.labeler.catch_label()
                    }],
                    "finally": [{
                        "type": "process",
                        "label": self.labeler.finally_label()
                    }]
                })

            elif isinstance(node, javalang.tree.ForStatement) or isinstance(node, javalang.tree.WhileStatement):
                steps.append({
                    "type": "loop",
                    "label": self.labeler.loop_label()
                })

            elif isinstance(node, javalang.tree.Assignment):
                var = getattr(node.expressionl, "member", "value")
                steps.append({
                    "type": "process",
                    "label": self.labeler.assignment_label(var)
                })

            elif isinstance(node, javalang.tree.StatementExpression):
                expr = node.expression
                name = getattr(expr, "member", "operation")
                steps.append({
                    "type": "process",
                    "label": self.labeler.method_call_label(name)
                })

        return steps

    def _block(self):
        return [{"type": "process", "label": "Continue process"}]
