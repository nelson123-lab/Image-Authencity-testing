# Image-Authencity-testing

The advancement of Computer vision have developed mulitple tools like stable diffusion and firefly which can generate Artificial images. This repository compares the difference between real images taken from a camera and images generated using stable diffusion. 

The images generated using stable diffusion will be lacking metadata while the images taken from a camera will be having it.

This is a naive mathod of testing the authencity of the image. The image taken on camera will only have the meta data information only if we have the original copy of the image or it is been transferred as a document. The image generated using a stable diffusion is lacking the metadata information. 

Existing Methods

- Hugging face provides an efficient AI image detector.
- [Maybe's AI Art Detector](https://huggingface.co/spaces/umm-maybe/AI-image-detector)

Efficient Methodology

- We can use a CNN to train the several images taken from a camera and equal number of images generated from stable diffusion.

References:

[Can an AI learn to identify “AI art”?](https://medium.com/@matthewmaybe/can-an-ai-learn-to-identify-ai-art-545d9d6af226)

