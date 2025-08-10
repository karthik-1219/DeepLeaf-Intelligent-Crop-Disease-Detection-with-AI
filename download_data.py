import gdown
import zipfile
import os

def download_and_extract():
    files = {
        "test": "1thjoIqHc8XHuNGMj7aMzEMGgwz8SoT7S",
        "train": "1_nnrSmZNUYfll_C9Q3zxdmh1bEymXgpq",
        "valid": "1YHD9AQ4mcADyeQU6ucqDApVTuI5niRbd"
    }

    for name, file_id in files.items():
        output = f"{name}_zip.zip"
        
        if not os.path.exists(output):
            print(f"Downloading {name} dataset...")
            gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
        
        extract_folder = f"./{name}"
        if not os.path.exists(extract_folder):
            print(f"Extracting {output}...")
            with zipfile.ZipFile(output, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            print(f"{name} extracted successfully.")

if __name__ == "__main__":
    download_and_extract()
