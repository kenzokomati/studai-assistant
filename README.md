# YouTube Transcript API with FastAPI

This project is a RESTful API built with FastAPI that retrieves video transcripts from YouTube. It utilizes the `YouTubeTranscriptApi` library to fetch transcripts in specified languages, with optional timestamp inclusion.

## Features

- Fetch YouTube video transcripts in multiple languages.
- Optionally include or exclude timestamps from the transcript text.

## Requirements

- Python 3.8+
- FastAPI
- YouTubeTranscriptApi
- OpenAI
- PyDantic

## Setup and Installation

1. **Clone the repository**

```bash
git clone https://github.com/kenzokomati/studai-assistant.git
cd studai-assistant
```

2. **Install requirements**

```bash
pip install -r requirements.txt
```

3. **Set enviroment variables**

```properties
OPENAI_ORGANIZATION_ID=<your_openai_organization_id>
OPENAI_PROJECT_ID=<your_openai_project_id>
OPENAI_API_KEY=<your_openai_api_key>
```

4. **Run the application**

Start the FastAPI application using uvicorn:

```bash
uvicorn main:app --reload
```

This will run the server at `http://127.0.0.1:8000`.

## Usage

Send a `GET` request to the root endpoint (`/`) with the following parameters:

`videoId`: (string, required) The YouTube video ID from which the transcript is to be retrieved.
`timestampEnabled`: (boolean, optional, default is `False`) If set to `True`, timestamps are included in the transcript. If set to `False`, timestamps are excluded, and only the text is returned.

### Example Request

```bash
GET http://127.0.0.1:8000/api/quiz?videoId=<video-id>&questions=1
```

### Example Response

```json
{
  "title": "Sample Quiz",
  "description": "A quiz based on a video transcript",
  "questions": [
    {
      "questionType": "MULTIPLE_CHOICE",
      "statement": "What is the capital of France?",
      "hint": "It's also known as the city of light",
      "explanation": "Paris is the capital and largest city of France.",
      "correctAnswer": 1,
      "options": ["Berlin", "Paris", "Rome", "Madrid"]
    }
  ]
}
```

## Dependencies

- **FastAPI**: For building and running the API.
- **YouTubeTranscriptApi**: For accessing YouTube video transcripts.
- **OpenAI**: For generate quizzes and check answers.

## License

This project is licensed under the MIT [License](LICENSE.txt).
