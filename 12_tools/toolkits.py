from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b


class MathToolKit:
    def get_tools(self):
        return [add, multiply]
