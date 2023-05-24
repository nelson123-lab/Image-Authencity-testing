from PIL import Image

# Open the image file
cam_image = Image.open('test.jpg')
stable_diffusion_image = Image.open('stable_test.jpg')
# Get the metadata
metadata1 = cam_image.getexif()
metadata2 = stable_diffusion_image.getexif()
# Print the metadata
print("Meta data of the image taken from camera",metadata1)
print("Meta data of the image taken from stable diffusion image", metadata2)


"""
Meta data of the image taken from camera 
{296: 2, 282: 72.0, 256: 4000, 257: 2252, 34665: 236, 271: 'samsung', 272: 'Galaxy S23 Ultra', 305: 'S918U1UES1AWC9', 274: 1, 306: '2023:05:23 19:52:19', 531: 1, 283: 72.0}
Meta data of the image taken from stable diffusion image {}
"""

