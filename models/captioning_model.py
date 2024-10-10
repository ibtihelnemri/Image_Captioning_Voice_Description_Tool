from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import streamlit as st

# Load pre-trained BLIP image captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_file):
    """
    Generate a caption for the uploaded image using BLIP model.
    """
    try: 
        # Open the image using PIL directly from the file-like object
        image = Image.open(image_file)

        # Preprocess the image with the BLIP processor
        inputs = processor(images=image, return_tensors="pt")

        # Generate the caption using the BLIP model
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption

    except Exception as e:
        st.error(f"Error generating caption: {str(e)}")
        return None
    