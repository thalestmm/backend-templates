from typing import Literal, Union

from langchain.tools import tool


@tool(
    name="calculator",
    description="Use this tool to calculate mathematical expressions. Always use this tool for any math problems",
)
def calculator(
    x: Union[int, float], y: Union[int, float], expression: Literal["+", "-", "*", "/"]
) -> str:
    if expression == "+":
        return str(x + y)
    elif expression == "-":
        return str(x - y)
    elif expression == "*":
        return str(x * y)
    elif expression == "/":
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return str(x / y)
    else:
        raise TypeError("Expression must be in [+, -, *, /]")
