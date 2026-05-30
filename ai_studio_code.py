import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

tools = [
    {
        'type': 'google_search',
    },
    {
        'type': 'url_context',
    },
]


interaction = client.interactions.create(
    agent='deep-research-preview-04-2026',
    input='',
    background=True,
    tools=tools,
    agent_config={
        'type': 'deep-research',
        'thinking_summaries': 'auto',
        'visualization': 'auto',
    },
)

for event in client.interactions.get(id=interaction.id, stream=True):
    if event.event_type == 'content.delta':
        if event.delta and event.delta.type == 'text':
            print(event.delta.text, end='')


