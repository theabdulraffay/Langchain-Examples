from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = 'Unknown' # Default value for name
    age: Optional[int] = None # Optional field for age
    email: EmailStr # Email field with validation

new_student= {
    "name": "John Doe",
    "age": 20,
    "email": "abc@gmail.com"
}

student = Student(**new_student)
print(student)