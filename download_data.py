import requests
import os
import zipfile

os.makedirs("data", exist_ok=True)

url = "https://static.nhtsa.gov/odi/ffdd/cmpl/FLAT_CMPL.zip"
zip_path = "data/FLAT_CMPL.zip"

print("Downloading NHTSA complaints dataset...")

response = requests.get(url, stream=True)
total = int(response.headers.get('content-length', 0))
downloaded = 0

with open(zip_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
        downloaded += len(chunk)
        if total:
            pct = downloaded / total * 100
            print(f"\rProgress: {pct:.1f}%", end='', flush=True)

print("\nDownload complete. Extracting...")

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall("data/")

print("Extraction complete.")
print("Files in data/:")
for f in os.listdir("data/"):
    size = os.path.getsize(f"data/{f}") / (1024*1024)
    print(f"  {f} — {size:.1f} MB")