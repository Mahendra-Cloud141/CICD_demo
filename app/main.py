from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to CI/CD demo!"}

@app.get("/add")
def add(a: int, b: int):
    """Simple addition route."""
    return {"sum": a + b}
