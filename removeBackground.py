from rembg import remove
from PIL import Image
import os

# Define input and output paths
input_path = 'tatianaDomitrovic.png' 
output_path = 'noBackground/tatianaDomitrovic.png' 

# Ensure the input file exists
if not os.path.exists(input_path):
    print(f"Error: Input file not found at {input_path}")
else:
    # Open the image using Pillow (PIL)
    input_image = Image.open(input_path)
    
    # Remove the background
    output_image = remove(input_image)
    
    # Save the resulting image with a transparent background (PNG format supports transparency)
    output_image.save(output_path)
    print(f"Background removed and saved to {output_path}")

