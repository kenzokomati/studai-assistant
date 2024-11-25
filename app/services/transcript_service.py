from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(videoId: str, timestampEnabled: bool = False):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId, languages=["en", "pt"])
        if not timestampEnabled:
            transcript = " ".join(line["text"] for line in transcript).strip()
        return {"transcript": transcript}
    except Exception as e:
        raise Exception("Transcript not found or unavailable.")
