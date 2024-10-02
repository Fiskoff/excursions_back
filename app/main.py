from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_hello():
    return {"string": "hello fastAPI"}
