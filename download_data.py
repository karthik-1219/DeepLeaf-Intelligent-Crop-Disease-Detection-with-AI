import gdown
import zipfile
import os

def download_and_extract():
    files = {
        "train.zip": "1_nnrSmZNUYfll_C9Q3zxdmh1bEymXgpq",
        "test.zip": "1thjoIqHc8XHuNGMj7aMzEMGgwz8SoT7S",
        "valid.zip": "1YHD9AQ4mcADyeQU6ucqDApVTuI5niRbd"
    }
    
    for filename, file_id in files.items():
        url = f"https://drive.google.com/uc?id={file_id}"
        if not os.path.exists(filename.replace(".zip", "")):  # avoid re-downloading
            gdown.download(url, filename, quiet=False)
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(filename.replace(".zip", ""))
            os.remove(filename)
