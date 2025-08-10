import os
import gdown
import zipfile

def download_and_extract():
    files = {
        "train_zip.zip": "1_nnrSmZNUYfll_C9Q3zxdmh1bEymXgpq",
        "test_zip.zip": "1thjoIqHc8XHuNGMj7aMzEMGgwz8SoT7S",
        "valid_zip.zip": "1YHD9AQ4mcADyeQU6ucqDApVTuI5niRbd"
    }

    for filename, file_id in files.items():
        # Only download if not already extracted
        folder_name = filename.replace("_zip.zip", "")
        if not os.path.exists(folder_name):
            print(f"Downloading {filename}...")
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, filename, quiet=False)

            print(f"Extracting {filename}...")
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(folder_name)

            print(f"{filename} extracted to {folder_name}/")
        else:
            print(f"{folder_name} already exists, skipping download.")

if __name__ == "__main__":
    download_and_extract()
