# screenie

Silly, maybe useful, GPT Vision watching your screen and narrating

## How it works

Screenie takes a screenshot every second and sends it to OpenAI's GPT-4 Vision model for analysis. The model then generates a description of the screenshot, which is printed to the terminal (in iTerm2 and hterm). After it's spoken out loud using a text-to-speech service.

## Installation

After cloning the repository, use `poetry` to install the project:

```
poetry install
```

## Usage

To start Screenie, run the main script

```
poetry run screenie
```

### Arguments

The `screenie` command accepts the following arguments:

- `--prompt`: Choice of default prompt. Default is "attenborough".
- `--voice`: Choice of voice.
- `--voice-provider`: Choice of voice provider. Options are "openai" and "elevenlabs". Default is "openai".
- `--screenshot`: Flag to indicate whether to take a screenshot. Default is False.
- `--picture`: Flag to indicate whether to take a picture. Default is False.

Please note that you can't take both a screenshot and a picture at the same time.

#### Examples

To run `screenie` with the default settings

```bash
screenie
```

To run `screenie` and take a screenshot:

```bash
screenie --screenshot
```

To run `screenie` and take a picture:

```bash
screenie --picture
```

To run `screenie` with a specific voice and voice provider:

```bash
screenie --voice "onyx" --voice-provider "openai"
```