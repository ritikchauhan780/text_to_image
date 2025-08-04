# DALL-E Style Image Generation Using Openai

API_KEY= "sk-proj-gbtbUnrz6FYuwKhmjfScTrVvxvxebcu4otFJRTw8CaqynFMZdAQ_PzCKwGvEgUZKZ4iJUlza3VT3BlbkFJrHHseAQOsRyMyFLGRQsIyq7CeXa-nbJCjcsV-hhvGG023g3mTDP1hVmOpVnOUKSb_Ko-GybwMA_AA"
import openai
import requests
from PIL import Image

# Login with your token (only needs to be run once per session)
def getImage():
    openai.api_key = API_KEY
    response = openai.Image.create(
        prompt = input("Which image you want to generate?"),
        n = 1,
        size = "1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

img_url = getImage()
res = requests.get(img_url)

with open("image.png", "wb")as image:
    image.write(res.content)

img = Image.open("image.png")
img.show()   
