import openai

def transcribe_audio(file_path):
    audio_file = open(file_path, "rb")

    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file
    )

    return transcript["text"]