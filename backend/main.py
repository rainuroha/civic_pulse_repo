
from fastapi import FastAPI

app = FastAPI(title="CivicPulse API")


@app.get("/")
def home():
    return {"message": "CivicPulse backend is running!"}