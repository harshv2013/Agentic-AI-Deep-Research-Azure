import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv(override=True)

azure_client = AzureOpenAI(
    api_key=os.getenv("openai-api-key"),
    azure_endpoint=os.getenv("openai-endpoint"),
    api_version=os.getenv("openai-api-version"),
)
DEPLOY = os.getenv("openai-deployment-name")

def azure_chat(instructions: str, prompt: str) -> str:
    """Run a chat completion against Azure OpenAI with system + user messages."""
    response = azure_client.chat.completions.create(
        model=DEPLOY,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content
