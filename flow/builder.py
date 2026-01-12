from flow.node import FlowNode


class FlowBuilder:

    def __init__(self):
        self.count = 0

    def _new(self, label, shape="process"):
        self.count += 1
        return FlowNode(f"N{self.count}", label, shape)

    def build_flow(self, steps):
        start = self._new("Start", "start_end")
        current = [start]

        for step in steps:
            t = step["type"]

            if t == "decision":
                node = self._new(step["label"], "decision")
                for c in current:
                    c.connect(node)

                yes = self._new("Yes path")
                no = self._new("No path")

                node.connect(yes, "Yes")
                node.connect(no, "No")

                current = [yes, no]

            elif t == "loop":
                node = self._new(step["label"])
                for c in current:
                    c.connect(node)
                node.connect(node, "Repeat")
                current = [node]

            else:
                node = self._new(step["label"])
                for c in current:
                    c.connect(node)
                current = [node]

        end = self._new("End", "start_end")
        for c in current:
            c.connect(end)

        return [start]
