from fastapi import FastAPI

app = FastAPI()

from youtube_transcript_api import YouTubeTranscriptApi

@app.get("/")
async def getVideoTranscript(videoId: str, timestampEnabled: bool = False):

  transcript = YouTubeTranscriptApi.get_transcript(videoId, languages=['en', 'pt'])

  if(not timestampEnabled):
    transcript = " ".join(line["text"] for line in transcript).strip()

  return {"transcript" : transcript}