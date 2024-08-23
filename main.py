from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    print("yes showing.....")
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
