# DALL-E Style Image Generation Using Hugging Face (Stable Diffusion)

from diffusers import StableDiffusionPipeline
import torch

# Load the model
# pipe = StableDiffusionPipeline.from_pretrained(
#    "CompVis/stable-diffusion-v1-4",
#    use_auth_token="hf_KmYvfSsAIECJxclfITNXjECgOxKYBSrawuVRt"  # Replace with your actual token from https://huggingface.co/settings/tokens
#)
from huggingface_hub import login

# Login with your token (only needs to be run once per session)
login("hf_GziDDmpqVRIDIDnkTFcOxmbuOfbJIADq")

# Load the model without the token parameter
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

# Move model to GPU if available
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Define your prompt
prompt = "A futuristic city in the clouds during sunset with flying cars"

# Generate image
image = pipe(prompt).images[0]

# Save image
image.save("huggingface_sd_image.png")
print("Image saved as 'huggingface_sd_image.png'")
