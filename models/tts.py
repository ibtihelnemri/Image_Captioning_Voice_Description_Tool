from gtts import gTTS
import os

def convert_text_to_speech(text, output_file="output.mp3", lang='en'):
    """
    Convert text to speech and save the audio as output.mp3.
    """
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_file)
        return True
    except Exception as e:
        return f"Error converting text to speech: {str(e)}"

def generate_instruction_audio(output_file="instruction_audio.mp3"):
    """
    Generate an instruction audio file and save it as output_file.
    """
    instruction_text = """
    Welcome to the Image Captioning with Voice Description Tool.
    Please upload an image, and we will generate a description and convert it into speech for you.
    """
    return convert_text_to_speech(instruction_text, output_file)