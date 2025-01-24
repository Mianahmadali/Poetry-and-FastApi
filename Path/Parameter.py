from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{name}/{age}/{Qualification}")
def greet(name: str, age:int , Qualification : str):
    try:
        return {
            "Status": "Success",
            "Data": f"Hello: {name}" , 
            "age" :  age ,
            "Qualification" : Qualification ,
        }
    except Exception as e:
        return {
            "Message": str(e),
            "Status": "error",
            "Data": None
        }

