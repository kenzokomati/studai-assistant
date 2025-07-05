from pydantic import BaseModel, Field
from typing import List, Union, Optional

class Message(BaseModel):
    role: str = Field(..., description="Role of the sender", enum=["user", "system", "assistant"])
    content: Union[str, List[dict]] = Field(..., description="Content of the message. Can be a string or a list of structured data.")