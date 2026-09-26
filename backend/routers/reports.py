from fastapi import APIRouter

router = APIRouter()


@router.get("/reports")
async def get_reports():
    return {
        "message": "SANKETRA reports endpoint is working",
        "reports": []
    }