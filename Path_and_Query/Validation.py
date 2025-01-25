from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int
    education: str  
    email: str

@app.post("/users/{id}")
def greet(person: Person ,id: int, q: Optional[str] = None ):
    try:
        if id < 100:
          raise ValueError("The Id Must be Greater then 100")
        return {
            "Status": "Success",
            "Data": {
                "id": id,
                "person": person,  
                "Query": q
            }
        }
    except Exception as e:
        return {
            "Message": str(e),
            "Status": "error",
            "Data": None
        }