from fastapi import FastAPI
#uvicorn firstapp:app --reload
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}