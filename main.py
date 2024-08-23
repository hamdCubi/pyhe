from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    print("yes showing.....")
    return {"message": "Hello, World!"}

