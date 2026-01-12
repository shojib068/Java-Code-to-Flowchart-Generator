class FlowNode:
    def __init__(self, id, label, shape="process"):
        self.id = id
        self.label = label
        self.shape = shape
        self.next_nodes = []

    def connect(self, node, label=None):
        self.next_nodes.append((node, label))
