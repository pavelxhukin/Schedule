from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI()

@app.get("/ping")
def pint():
    return {"Success:":True}