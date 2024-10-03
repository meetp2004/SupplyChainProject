import os
from google.cloud import storage

def upload_to_gcs(bucket_name, source_folder, target_folder):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, source_folder)
            blob_path = os.path.join(target_folder, relative_path)
            blob = bucket.blob(blob_path)
            blob.upload_from_filename(file_path)
            print(f"Uploaded {file} to GCS bucket '{bucket_name}'.")

if __name__ == "__main__":

    # Upload to GCS
    bucket_name = "supplydata"
    upload_to_gcs(bucket_name, './data/', 'data/')