from fastapi import FastAPI
from backend.routers import reports

app = FastAPI()

app.include_router(reports.router)


@app.get("/")
async def root():
    return {"message": "SANKETRA backend is running"}