import time

import click
from openai import OpenAI

from .audio import play_audio
from .imaging import analyze_image, take_screenshot

client = OpenAI()


@click.command()
@click.option("--prompt", default="attenborough", help="Choice of default prompt")  # noqa
@click.option("--voice", help="Choice of voice")
@click.option(
    "--voice-provider",
    type=click.Choice(["openai", "elevenlabs"]),
    default="openai",
    help="Choice of voice provider",
)
@click.option(
    "--screenshot",
    "wants_screenshot",
    is_flag=True,
    help="Whether to take a screenshot",
)
@click.option(
    "--picture", "wants_picture", is_flag=False, help="Whether to take a picture"  # noqa
)
def main(prompt, voice, voice_provider, wants_screenshot, wants_picture):
    script = []

    print("Ready in 3...", end="", flush=True)
    time.sleep(1)
    print("2...", end="", flush=True)
    time.sleep(1)
    print("1...", end="", flush=True)
    time.sleep(1)

    # TODO: `play()` a starting sound

    while True:
        if wants_picture:
            raise NotImplementedError("Picture taking not yet implemented")
        else:  # wants_screenshot is the default
            base64_image = take_screenshot()

        # analyze screen
        print("👀 Watching...")

        # Write the image to the terminal using iTerm2 inline images protocol
        print("\033]1337;File=;inline=1:" + base64_image + "\a")
        time.sleep(0.5)

        analysis = analyze_image(
            base64_image,
            script=script,
            prompt=prompt,
        )

        print("🎙️ David says:")
        print(analysis)

        play_audio(analysis, provider=voice_provider, voice=voice)

        # Disabling to save tokens and $$$
        # script = script + [{"role": "assistant", "content": analysis}]

        time.sleep(1)


# Run the main function
if __name__ == "__main__":
    main()
