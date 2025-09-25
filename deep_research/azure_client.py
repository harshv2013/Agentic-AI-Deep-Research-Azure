import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv(override=True)

azure_client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    api_version=os.getenv("OPENAI_API_VERSION"),
)
DEPLOY = os.getenv("OPENAI_DEPLOYMENT_NAME")

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
