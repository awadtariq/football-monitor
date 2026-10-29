from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Football Match Analytics Platform backend is online!"}