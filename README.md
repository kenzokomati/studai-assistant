# StudAI Assistant - Python Backend

![Python](https://img.shields.io/badge/python-3.9%20%7C%203.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.3-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository contains the **Python FastAPI microservice** for the Studai project, an AI-driven quiz creation platform. This service handles two core functionalities:
1. **YouTube Transcript Retrieval**: Fetches transcripts for YouTube videos
2. **AI-Powered Quiz Generation**: Creates quizzes from various sources using OpenAI's GPT models

## ✨ Key Features
- **YouTube Transcript API**: Retrieve video transcripts with optional timestamps
- **Quiz Generation**: Create quizzes from text prompts, YouTube videos, or PDF content
- **Multi-language Support**: Generate quizzes in English (EN) or Portuguese (PT)
- **PDF Processing**: Extract content from uploaded PDF files
- **Structured Logging**: Request tracing with unique IDs
- **Authentication**: Secure endpoints with bearer token authentication

## 📂 Project Structure
```text
├── .dockerignore
├── .github
│ └── workflows
│ └── python-api-ci-cd.yml # CI/CD pipeline
├── .gitignore
├── Dockerfile # Container configuration
├── Dockerrun.aws.json # Elastic Beanstalk config
├── LICENSE
├── app
│ ├── api
│ │ └── v1
│ │ ├── quiz.py # Quiz endpoints
│ │ └── transcript.py # Transcript endpoints
│ ├── clients
│ │ └── openai_client.py # OpenAI integration
│ ├── context.py # Request context
│ ├── logger.py # Logging configuration
│ ├── main.py # App entrypoint
│ ├── middleware
│ │ └── logging.py # Request logging
│ ├── prompts
│ │ └── quiz_generation_instructions.md # AI instructions
│ ├── schemas # Pydantic models
│ │ ├── message.py
│ │ ├── question.py
│ │ ├── quiz.py
│ │ └── quiz_request.py
│ ├── services
│ │ ├── file_service.py # PDF processing
│ │ ├── quiz_service.py # Quiz generation
│ │ └── transcript_service.py # YouTube transcripts
│ └── utils
│ └── prompts.py # Prompt utilities
└── requirements.txt # Dependencies
```


## 🚀 Technology Stack
- **Python 3.12** (with support for 3.9+)
- **FastAPI** - API framework
- **OpenAI API** - Quiz generation

## 🛠️ Getting Started
### Prerequisites
- Python 3.9+
- OpenAI API key
- Docker (optional)

### Local Setup
#### 1. Clone the repository:
```bash
git clone https://github.com/kenzokomati/studai-assistant.git
cd studai-assistant
```

#### 2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

#### 4. Run the application:
```bash
uvicorn app.main:app --reload --port 8000
```

### Configuration
Create a `.env` file:
```properties
OPENAI_ORGANIZATION_ID=<your_org_id>
OPENAI_PROJECT_ID=<your_project_id>
OPENAI_API_KEY=<your_api_key>
SECURITY_KEY=dev_key
```

## 🌐 API Documentation
Interactive API documentation is available at:
`http://localhost:8000/docs`

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

