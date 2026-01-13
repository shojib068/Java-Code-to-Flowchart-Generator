from parser.java_parser import JavaCodeParser
from flow.builder import FlowBuilder
from diagram.mermaid import generate_mermaid

def escape_label(label: str) -> str:
    """
    Escape special characters for Mermaid node labels.
    - Converts double quotes " to single quotes '
    - Escapes &, <, >
    """
    if label is None:
        return ""
    # Convert all double quotes to single quotes
    label = label.replace('"', "'")
    # Escape special HTML characters for Mermaid safety
    label = label.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return label

def java_code2flow(code: str) -> str:
    parser = JavaCodeParser()
    steps = parser.parse(code)

    # Escape all step labels to convert "..." -> '...'
    for step in steps:
        if hasattr(step, "label") and step.label:
            step.label = escape_label(step.label)

    builder = FlowBuilder()
    start_node = builder.build_flow(steps)[0]

    return generate_mermaid(start_node)
