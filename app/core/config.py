import os
from openai import OpenAI

client = OpenAI(
    organization=os.environ.get("OPENAI_ORGANIZATION_ID"),
    project=os.environ.get("OPENAI_PROJECT_ID"),
)
