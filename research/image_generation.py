import boto3
import json
import base64

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = """
A futuristic cyberpunk city at night with neon lights,
flying cars, cinematic lighting, ultra-detailed, 4K
"""

payload = {
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": prompt
    },
    "imageGenerationConfig": {
        "numberOfImages": 1,
        "height": 512,
        "width": 512,
        "cfgScale": 8.0,
        "seed": 42
    }
}

response = bedrock.invoke_model(
    modelId="amazon.titan-image-generator-v2:0",
    body=json.dumps(payload),
    accept="application/json",
    contentType="application/json"
)


response_body = json.loads(response["body"].read())


image_base64 = response_body["images"][0]
image_bytes = base64.b64decode(image_base64)


with open("generated_image.png", "wb") as f:
    f.write(image_bytes)

print("✅ Image generated successfully: generated_image.png")
