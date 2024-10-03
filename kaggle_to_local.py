import os
import kaggle
from zipfile import ZipFile

def download_kaggle_data(dataset_name, download_path):
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Download the dataset from Kaggle
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Dataset '{dataset_name}' downloaded and extracted to '{download_path}'.")

if __name__ == "__main__":
    # Replace 'dataset-name' with the actual Kaggle dataset path you want to use
    dataset_name = "bytadit/ecommerce-order-dataset"
    
    # Specify where to download the data
    download_path = "./data/"

    # Download and extract the data
    download_kaggle_data(dataset_name, download_path)