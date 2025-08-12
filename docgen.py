from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from parser import endpoints
import json
from getpass import getpass

client = InferenceClient(
    model = "openai/gpt-oss-120b",
)

def hf_query(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]