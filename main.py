from parser.java_parser import JavaCodeParser
from flow.builder import FlowBuilder
from diagram.mermaid import generate_mermaid


def java_code2flow(code: str) -> str:
    parser = JavaCodeParser()
    steps = parser.parse(code)

    builder = FlowBuilder()
    start = builder.build_flow(steps)[0]

    return generate_mermaid(start)
