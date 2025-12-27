import boto3
import json

prompt_data = """
Provide the AWS services used for Generative AI along with a brief description for each service.
"""

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

payload = {
    "prompt": f"<s>[INST] {prompt_data} [/INST]",
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9
}

response = bedrock.invoke_model(
    modelId="meta.llama3-70b-instruct-v1:0",
    body=json.dumps(payload),
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response["body"].read())
print(response_body["generation"])
