import streamlit as st
import os
from models.captioning_model import generate_caption
from models.tts import generate_instruction_audio, convert_text_to_speech
from PIL import Image

# Generate the instruction audio (only generate if the file doesn't already exist)
if not os.path.exists("instruction_audio.mp3"):
    generate_instruction_audio()

# Streamlit App Title
st.title("Image Captioning with Voice Description")

# Brief explanation of the application
st.write("""
This application utilizes image captioning and text-to-speech models to generate a caption for an uploaded image and convert the caption into speech.
The image captioning model is based on [Salesforce's BLIP architecture](https://huggingface.co/Salesforce/blip-image-captioning-base), which can generate descriptive captions for images.
The text-to-speech model, based on gTTS, converts the generated caption into speech.
""")

# Sidebar for audio instructions
st.sidebar.title("Instructions")
st.sidebar.write("Click below to hear the instructions on how to use the app.")

if st.sidebar.button("Play Instructions"):
    if os.path.exists("instruction_audio.mp3"):
        st.sidebar.audio('instruction_audio.mp3')

# File uploader for images with descriptive alt-text
uploaded_file = st.file_uploader("Upload an image (jpg, png, jpeg)...", type=["jpg", "png", "jpeg"], help="Upload an image for captioning")

if uploaded_file is not None:
    # Display additional file info
    file_details = {
        "Filename": uploaded_file.name,
        "File Type": uploaded_file.type,
        "File Size": f"{uploaded_file.size / 1024:.2f} KB"
    }
    st.write(file_details)

    # Display the uploaded image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True, output_format="JPEG")

    # Provide descriptive text for accessibility
    st.write("Description: User-uploaded image for captioning.")

    # Generate caption for the image with a spinner
    with st.spinner('Generating caption...'):
        caption = generate_caption(uploaded_file)  # Removed max_length argument
    st.success('Caption generated!')
    st.write(f"Caption: {caption}")

    # Convert the generated caption to speech with a spinner
    with st.spinner('Converting caption to speech...'):
        output_audio_file = "output.mp3"
        result = convert_text_to_speech(caption, output_file=output_audio_file, lang='en')

    if isinstance(result, str):
        st.error(result)
    else:
        st.success("Caption converted to speech!")
        st.audio(output_audio_file)

# Footer for contact and additional links
st.markdown("---")
st.write("Developed by Ibtihel Nemri. [GitHub](https://github.com/ibtihelnemri?tab=repositories)")
