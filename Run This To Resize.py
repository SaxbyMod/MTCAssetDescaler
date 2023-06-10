import os
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)

def resize_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            logging.info(f"Importing image: {input_path}")
            
            with Image.open(input_path) as image:
                resized_image = image.resize((448, 448), Image.LANCZOS)
                resized_image.save(output_path, quality=95)

            logging.info(f"Image exported: {output_path}")

# Example usage
input_folder = "Old"
output_folder = "New"

resize_images(input_folder, output_folder)
