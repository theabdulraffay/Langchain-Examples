from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

class AddInput(BaseModel):
    a: int = Field(required = True, description="The first number to add.")
    b: int = Field(required = True, description="The second number to add.")



def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


add_tool = StructuredTool.from_function(
    func=add,
    name="add",
    description="Adds two numbers.",
    args_schema=AddInput,

)

result = add_tool.invoke({
    "a": 5,
    "b": 3
})

print(f"The result of adding 5 and 3 is: {result}")
print(type(result))
print(f"{add_tool.name}")
print(f"{add_tool.description}")
print(f"{add_tool.args}")
print(f"{add_tool.args_schema.model_json_schema()}")