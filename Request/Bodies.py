from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int
    education: str  
    email: str

@app.post("/users")
def greet(person: Person):
    try:
        return {
            "Status": "Success",
            "Data": person
        }
    except Exception as e:
        return {
            "Message": str(e),
            "Status": "error",
            "Data": None
        }