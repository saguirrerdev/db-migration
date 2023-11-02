from fastapi import FastAPI
from routers import departments, jobs, hired_employees

app = FastAPI()

app.include_router(departments.router, prefix="/departments", tags=["departments"])   
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])   
app.include_router(hired_employees.router, prefix="/hired_employees", tags=["hired_employees"])   

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, env_file="app/.env")
