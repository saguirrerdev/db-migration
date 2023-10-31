from fastapi import FastAPI
from routers import departments

app = FastAPI()

app.include_router(departments.router, prefix="/departments", tags=["departments"])   

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
