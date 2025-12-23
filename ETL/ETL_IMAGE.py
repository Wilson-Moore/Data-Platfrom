from PIL import Image
import pytesseract
from dotenv import dotenv_values


ENV_KEYS=dotenv_values(".env")

image=Image.open(f"{ENV_KEYS.get("IMAGES_PATH")}/order_001.jpg")

text=pytesseract.image_to_string(image)

print(text)