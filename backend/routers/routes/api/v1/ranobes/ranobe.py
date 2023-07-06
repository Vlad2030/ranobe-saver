from fastapi import APIRouter

router = APIRouter(tags=["ranobes"])

@router.get(
    path="/",
    status_code=200,
    summary="Get ranobe",
    description="Get ranobe from mangalib.me (´♡‿♡`)",
)
async def get_ranobe():
    return {"ok": True}