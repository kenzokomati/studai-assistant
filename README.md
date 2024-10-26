# YouTube Transcript API with FastAPI

This project is a RESTful API built with FastAPI that retrieves video transcripts from YouTube. It utilizes the `youtube_transcript_api` library to fetch transcripts in specified languages, with optional timestamp inclusion.

## Features

- Fetch YouTube video transcripts in multiple languages.
- Optionally include or exclude timestamps from the transcript text.

## Requirements

- Python 3.8+
- FastAPI
- youtube_transcript_api

## Setup and Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Create a virtual environment and activate it**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install fastapi youtube_transcript_api uvicorn
```

4. **Run the application**

Start the FastAPI application using uvicorn:

```bash
uvicorn main:app --reload
```

This will run the server at ```http://127.0.0.1:8000```.

## Usage
Send a ```GET``` request to the root endpoint (```/```) with the following parameters:

```videoId```: (string, required) The YouTube video ID from which the transcript is to be retrieved.
```timestampEnabled```: (boolean, optional, default is ```False```) If set to ```True```, timestamps are included in the transcript. If set to ```False```, timestamps are excluded, and only the text is returned.

### Example Request

```http
  GET http://127.0.0.1:8000/?videoId=<video-id>&timestampEnabled=false
```

### Example Response
```json
{
  "transcript": "This is a sample transcript text."
}
```

## Dependencies
- **FastAPI**: For building and running the API.
- **youtube_transcript_api**: For accessing YouTube video transcripts.

## License
This project is licensed under the MIT License.