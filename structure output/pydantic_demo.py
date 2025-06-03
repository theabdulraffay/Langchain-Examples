from pydantic import BaseModel,EmailStr, Field
from typing import Optional


#Pydantic is a data validation and settings management library for Python.
# It uses Python type annotations to validate data and provides a way to define data models.

class Student(BaseModel):
    name: str = 'Unknown' # Default value for name
    age: Optional[int] = None # Optional field for age
    email: EmailStr # Email field with validation
    cgpa: float = Field(gt=0, le=10, default=5, description="Decimal value representing the cgpa of the student") # CGPA must be greater than 0 and less than or equal to 10

new_student= {
    "name": "John Doe",
    "age": 20,
    "email": "abc@gmail.com"
}

student = Student(**new_student)
print(student)

student_dist = student.model_dump_json()
print(type(student_dist))