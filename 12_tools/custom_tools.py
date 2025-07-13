from langchain_core.tools import tool


# add type hinting and doc string to the function, also add the tool decorator

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

result = add.invoke({
    "a": 5,
    "b": 3
})

print(f"The result of adding 5 and 3 is: {result}")
print(f"{add.name}")
print(f"{add.description}")
print(f"{add.args}")
print(f"{add.args_schema.model_json_schema()}")



