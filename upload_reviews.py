# upload_reviews.py
import json
from azure.storage.blob import BlobServiceClient
from config import AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME, BLOB_NAME

def upload_to_azure_blob(reviews):
    try:
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

        # Get a reference to the container and blob
        container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)
        blob_client = container_client.get_blob_client(BLOB_NAME)

        # Convert reviews to JSON and upload to blob
        json_data = json.dumps(reviews, ensure_ascii=False, indent=4)
        blob_client.upload_blob(json_data, overwrite=True)
        print(f"Reviews uploaded successfully to Azure Blob Storage as {BLOB_NAME}")

    except Exception as e:
        print(f"Error uploading to Azure Blob Storage: {e}")
