from rembg import remove
from PIL import Image

# Load the input image
input_path = 'input_image.jpg'  # Replace with your image path if different
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the output image
output_image.save('output_image.png')  # PNG format keeps transparency

# Optional: Show the resulting image
output_image.show()
