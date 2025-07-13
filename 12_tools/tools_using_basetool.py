from langchain.tools import BaseTool
from pydantic import Field, BaseModel
from typing import Type 

class addInput(BaseModel):
    a: int = Field(required = True, description="The first number to add.")
    b: int = Field(required = True, description="The second number to add.")


class AddTool(BaseTool):
    name: str = "add"
    description: str = "Adds two numbers."
    args_schema: Type[BaseModel] = addInput

    def _run(self, a: int, b: int) -> int:
        """Adds two numbers."""
        return a + b

    async def _arun(self, a: int, b: int) -> int:
        """Adds two numbers asynchronously."""
        return self._run(a, b)



add_tool = AddTool()
result = add_tool.invoke({
    "a": 5,
    "b": 3
})
print(f"The result of adding 5 and 3 is: {result}")