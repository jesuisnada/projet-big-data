import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob storage v12 - Python quickstart sample")
    # Quick start code goes here
    connect_str = os.getenv('CONNECT_STR')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # creer le nom du containeur
    container_name = "quickstart"

    # Create the container
    #container_client = blob_service_client.create_container(container_name)
    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='test.txt')

    #print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open('test.txt', "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)
