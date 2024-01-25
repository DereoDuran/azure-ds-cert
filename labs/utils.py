from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import os

subscription_id = os.getenv("SUBSCRIPTION_ID")
resource_group = os.getenv("RESOURCE_GROUP")
workspace = os.getenv("WORKSPACE")

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)