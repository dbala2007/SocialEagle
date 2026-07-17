from fastapi import FastAPI

app = FastAPI(
    title="Basic FastAPI Application",
    description="A simple FastAPI application that demonstrates basic functionality.",
    version="1.0.0"
)

@app.get("/")
def root():
    return """
    <h1>Welcome to the Basic FastAPI Application</h1>
    <p>Go to <a href="/docs">docs</a> to view the documentation.</p>
    """

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}