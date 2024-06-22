
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/simple")
def get_log_files(name: str):
    return {"name": name, "message": "success"}