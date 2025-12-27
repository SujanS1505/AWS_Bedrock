import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.invoke_model(
    modelId="amazon.titan-text-express-v1",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({
        "inputText": "Explain AWS Bedrock in simple terms",
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.7,
            "topP": 0.9
        }
    })
)

result = json.loads(response["body"].read())
print(result["results"][0]["outputText"])
