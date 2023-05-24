from PIL import Image

# Open the image file
image = Image.open('test.jpg')

# Get the metadata
metadata = image.getexif()

# Print the metadata
print(metadata)
