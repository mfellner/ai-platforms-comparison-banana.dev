import base64
import os
from datetime import datetime
from textwrap import dedent

import banana_dev as client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Create a reference to your model on Banana
my_model = client.Client(
    api_key=os.getenv("BANANA_API_KEY"),
    model_key=os.getenv("BANANA_MODEL_KEY"),
    url=os.getenv("BANANA_MODEL_URL"),
)

prompt = (
    dedent(
        """\
        hero in the woods with a cape and ((sword)),
        cartoon, disney, glowing, ethereal aura, bright,
        colorful, vibrant, fantasy, trending on Artstation
        """
    )
    .strip()
    .replace("\n", " ")
)

# Specify the model's input JSON, what you expect
# to receive in your Potassium app. Here is an
# example for a basic BERT model:
inputs = {"prompt": prompt}

# Call your model's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first
# method argument ("/")to specify a
# different route.
print("Calling model...")
result, meta = my_model.call("/", inputs)

print(meta)

base64str = result["output"]
image = base64.b64decode(base64str, validate=True)

# Convert the base64 string to an image and save it to disk
timestamp = str(int(datetime.utcnow().timestamp()))
file_name = f"output_{timestamp}.jpg"
with open(file_name, "wb") as f:
    f.write(image)
print(f"Saved image to {file_name}")
