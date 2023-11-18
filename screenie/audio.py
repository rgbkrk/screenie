import os
from typing import Literal, Optional

from elevenlabs import generate, play
from openai import OpenAI
from ulid import ULID

client = OpenAI()

# These are mine, you'll have to pass your own
fry_voice = "6EvaNCRRpIUj6wm59JYE"
attenborough_voice = "KhkNiIv7qAHQvKZrBvoJ"


def play_audio(
    text: str,
    provider=Literal["openai", "elevenlabs"],
    voice: Optional[str] = None
):
    audio: bytes

    if provider == "openai":
        response = client.audio.speech.create(
            model="tts-1",
            voice="fable" if voice is None else voice,  # type: ignore
            input=text,
        )

        audio = response.read()

    elif provider == "elevenlabs":
        generated_audio = generate(
            api_key=os.environ.get("ELEVENLABS_API_KEY"),
            text=text,
            voice=attenborough_voice if voice is None else voice,
            model="eleven_turbo_v2",
        )

        if isinstance(generated_audio, bytes):
            audio = generated_audio
        elif isinstance(generated_audio, (bytearray, memoryview)):
            audio = bytes(generated_audio)
        else:
            raise TypeError("Unexpected type for generated audio")
    else:
        raise ValueError(f"Unknown provider: {provider}")

    unique_id = ULID()
    dir_path = os.path.join("narration", str(unique_id))
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "audio.wav")

    with open(file_path, "wb") as f:
        f.write(audio)

    play(audio)
