from fastapi import APIRouter, HTTPException
from app.services.transcript_service import get_transcript

router = APIRouter()

@router.get("/")
async def get_transcript_endpoint(videoId: str, timestampEnabled: bool = False):
    try:
        return get_transcript(videoId, timestampEnabled)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

