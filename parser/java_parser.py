import javalang
from parser.label_generator import HumanLabelGenerator


def escape_label(label: str) -> str:
    """
    Escape special characters for Mermaid node labels.
    - Convert double quotes " to single quotes '
    - Escape &, <, >
    """
    if label is None:
        return ""
    label = label.replace('"', "'")
    label = label.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return label


class JavaCodeParser:

    def __init__(self):
        self.labeler = HumanLabelGenerator()

    def parse(self, code):
        tree = javalang.parse.parse(code)
        steps = []

        for _, node in tree:

            # ---------------- Method Declaration ----------------
            if isinstance(node, javalang.tree.MethodDeclaration):
                steps.append({
                    "type": "process",
                    "label": escape_label(self.labeler.method_label(node.name))
                })

            # ---------------- If Statement ----------------
            elif isinstance(node, javalang.tree.IfStatement):
                steps.append({
                    "type": "decision",
                    "label": escape_label(self.labeler.if_label(node.condition)),
                    "branches": self._block(),
                    "else": self._block()
                })

            # ---------------- Try Statement ----------------
            elif isinstance(node, javalang.tree.TryStatement):
                steps.append({
                    "type": "try",
                    "label": escape_label(self.labeler.try_label()),
                    "try": self._block(),
                    "catch": [{
                        "type": "exception",
                        "label": escape_label(self.labeler.catch_label())
                    }],
                    "finally": [{
                        "type": "process",
                        "label": escape_label(self.labeler.finally_label())
                    }]
                })

            # ---------------- Loops ----------------
            elif isinstance(node, javalang.tree.ForStatement) or isinstance(node, javalang.tree.WhileStatement):
                steps.append({
                    "type": "loop",
                    "label": escape_label(self.labeler.loop_label())
                })

            # ---------------- Assignment ----------------
            elif isinstance(node, javalang.tree.Assignment):
                var = getattr(node.expressionl, "member", "value")
                steps.append({
                    "type": "process",
                    "label": escape_label(self.labeler.assignment_label(var))
                })

            # ---------------- Statement Expression (method calls) ----------------
            elif isinstance(node, javalang.tree.StatementExpression):
                expr = node.expression
                name = getattr(expr, "member", "operation")
                steps.append({
                    "type": "process",
                    "label": escape_label(self.labeler.method_call_label(name))
                })

        return steps

    # ---------------- Block Placeholder ----------------
    def _block(self):
        return [{"type": "process", "label": escape_label("Continue process")}]
