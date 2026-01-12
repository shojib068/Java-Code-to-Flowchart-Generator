import re

def safe(text):
    return re.sub(r"[{}()=]", "", text)

def shape(node):
    label = safe(node.label)
    if node.shape == "decision":
        return f"{{{label}}}"
    return f"[{label}]"

def generate_mermaid(start):
    lines = ["flowchart TD"]
    seen = set()
    stack = [start]

    while stack:
        n = stack.pop()
        if n.id not in seen:
            lines.append(f"    {n.id}{shape(n)}")
            seen.add(n.id)

        for nxt, lbl in n.next_nodes:
            if lbl:
                lines.append(f"    {n.id} -->|{lbl}| {nxt.id}")
            else:
                lines.append(f"    {n.id} --> {nxt.id}")
            if nxt.id not in seen:
                stack.append(nxt)

    return "\n".join(lines)
