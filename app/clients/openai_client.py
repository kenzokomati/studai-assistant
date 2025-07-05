import os
from openai import OpenAI
from dotenv import load_dotenv

from app.schemas.message import Message

load_dotenv()

openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    organization=os.environ.get("OPENAI_ORGANIZATION_ID"),
    project=os.environ.get("OPENAI_PROJECT_ID"),
)

model="gpt-4o-mini"

def requestChatCompletion(messages: Message, response_format=None):
    response = openai_client.beta.chat.completions.parse(
        model=model,
        messages=messages,
        response_format=response_format,
    )
    return response.choices[0].message.parsed