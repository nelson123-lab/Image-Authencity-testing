from PIL import Image

# Open the image file
cam_image = Image.open('test.jpg')
stable_diffusion_image = Image.open('stable_test.jpg')
# Get the metadata
metadata1 = cam_image.getexif()
metadata2 = stable_diffusion_image.getexif()
# Print the metadata
print(metadata)
