from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "سلام! Trend Aggregator کار میکنه!"}