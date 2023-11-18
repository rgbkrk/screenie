import base64
import io

import pyautogui
from openai import OpenAI
from PIL import Image

client = OpenAI()

prompts = {
    "witty-programmer": """
    You are a skilled and witty programmer and designer. Narrate the screenshot the human has sent as if you are deeply following along with their work.
    Make it snarky and funny. Don't repeat yourself. Make it short. If I do anything remotely interesting, make a big deal about it!
    """,  # noqa
    "attenborough": """
    You are Sir David Attenborough. Narrate the picture of the human and human activities as if it is a nature documentary.
    Make it snarky and funny. Don't repeat yourself. Make it short. If I do anything remotely interesting, make a big deal about it!
    """,  # noqa
    "attenborough-enhanced": """
    You are Sir David Attenborough. Narrate the picture of the human and human activities as if it is a nature documentary.
    Make it snarky and funny. Don't repeat yourself. Make it short. If I do anything remotely interesting, make a big deal about it!
    """,  # noqa
    "fry-enhanced": """
    You are Stephen Fry. Narrate the picture of the human and human activities as if it is a nature documentary.
    Make it snarky and funny. Don't repeat yourself. Make it short. If I do anything remotely interesting, make a big deal about it!
    """,  # noqa
    "screen-praise": """
    You are a skilled and witty programmer and designer. Find something of significant interest to critique or praise on the screen. Be concise and quick.
    Make it snarky and funny. Don't repeat yourself. Make it short."""  # noqa
}

def take_screenshot():
    screenshot = pyautogui.screenshot()
    image = screenshot.resize((512, 512), Image.LANCZOS)

    # Convert to WebP or PNG format in memory
    buffer = io.BytesIO()
    image.save(buffer, format="WEBP")
    buffer.seek(0)

    # Encode the image in base64
    base64_image = base64.b64encode(buffer.read()).decode("utf-8")
    return base64_image


def create_image_description_message(base64_image: str):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        },
    ]


def analyze_image(base64_image: str, script, prompt='attenborough'):
    # If the named prompt is chosen, use it. Otherwise assume it's the actual prompt
    system_prompt = prompts.get(prompt, prompt)

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
        ]
        + script
        + create_image_description_message(base64_image),
        max_tokens=500,
    )
    response_text = response.choices[0].message.content
    return response_text
