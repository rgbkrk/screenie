import time

from openai import OpenAI

from .audio import play_audio
from .imaging import FRY_ENHANCED, analyze_image, take_screenshot

client = OpenAI()

def main():

    script = []

    print("Ready in 3...", end="", flush=True)
    time.sleep(1)
    print("2...", end="", flush=True)
    time.sleep(1)
    print("1...", end="", flush=True)
    time.sleep(1)

    while True:
        base64_image = take_screenshot()

        # analyze screen 
        print("👀 David is watching...")

        # Write the image to the terminal using iTerm2 inline images protocol
        print("\033]1337;File=;inline=1:" + base64_image + "\a")
        time.sleep(0.5)

        analysis = analyze_image(
            base64_image,
            script=script,
            prompt=FRY_ENHANCED,  # noqa
        )

        print("🎙️ David says:")
        print(analysis)

        play_audio(analysis, provider="openai")

        # script = script + [{"role": "assistant", "content": analysis}]

        time.sleep(1)


# Run the main function
if __name__ == "__main__":
    main()
