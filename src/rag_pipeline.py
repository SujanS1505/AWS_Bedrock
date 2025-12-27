from langchain_aws import ChatBedrock
import os

def get_llm():
    return ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        region_name=os.getenv("AWS_REGION")
    )
