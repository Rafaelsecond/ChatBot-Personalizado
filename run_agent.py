# Before running the sample:
#    pip install "azure-ai-projects>=2.1.0"

import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = os.environ.get("FOUNDRY_PROJECT_ENDPOINT")
agent_name = os.environ.get("FOUNDRY_AGENT_NAME")

missing_settings = [
    name
    for name, value in {
        "FOUNDRY_PROJECT_ENDPOINT": endpoint,
        "FOUNDRY_AGENT_NAME": agent_name,
    }.items()
    if not value
]
if missing_settings:
    missing = ", ".join(missing_settings)
    raise RuntimeError(
        f"Missing required environment variable(s): {missing}. "
        "Configure them in your local .env file."
    )

user_message = input("Digite sua mensagem: ")

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    # Bind the OpenAI client to the existing agent endpoint.
    openai_client = project_client.get_openai_client(agent_name=agent_name)

    # GitHub Copilot preview agents require a conversation for every Responses turn.
    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input=[{"role": "user", "content": user_message}],
    )

    print(f"Response output: {response.output_text}")
