from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def greet(q:str , name :str , age : int , Qualification : str ):
    try:
        return {
            "Status": "Success",
            "Data": f"Hello: {name}" , 
            "age" :  age ,
            "Qualification" : Qualification ,
            "Quary" : q
        }
    except Exception as e:
        return {
            "Message": str(e),
            "Status": "error",
            "Data": None
        }
