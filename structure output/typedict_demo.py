from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    is_student: bool



new_person: Person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}