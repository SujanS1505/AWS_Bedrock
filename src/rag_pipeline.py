from langchain_aws import ChatBedrock
import os

def get_llm():
    return ChatBedrock(
        model_id="amazon.titan-text-express-v1",
        region_name=os.getenv("AWS_REGION")
    )
