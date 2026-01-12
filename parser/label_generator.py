class HumanLabelGenerator:

    def method_label(self, name):
        return f"Start {self._split(name)} process"

    def if_label(self, condition):
        return f"Check whether {self._condition_to_text(condition)}"

    def try_label(self):
        return "Attempt to process safely"

    def catch_label(self):
        return "Handle error if something goes wrong"

    def finally_label(self):
        return "Perform final cleanup steps"

    def assignment_label(self, var):
        return f"Store value into {self._split(var)}"

    def method_call_label(self, name):
        return f"Perform action: {self._split(name)}"

    def loop_label(self):
        return "Repeat processing steps"

    def _condition_to_text(self, condition):
        if hasattr(condition, "operator"):
            left = self._condition_to_text(condition.operandl)
            right = self._condition_to_text(condition.operandr)
            op = condition.operator

            mapping = {
                "||": "or",
                "&&": "and",
                "==": "is equal to",
                "!=": "is not equal to",
                ">": "is greater than",
                "<": "is less than"
            }
            return f"{left} {mapping.get(op, op)} {right}"

        if hasattr(condition, "member"):
            return self._split(condition.member)

        if hasattr(condition, "value"):
            return "null" if condition.value is None else str(condition.value)

        return "condition is met"

    def _split(self, text):
        return "".join(
            [" " + c.lower() if c.isupper() else c for c in text]
        ).strip()
