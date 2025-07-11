import requests
import os
import zipfile
from io import BytesIO

# Use token from .env
SKETCHFAB_API_TOKEN = os.getenv("SKETCHFAB_API_TOKEN")

def download_model(model_uri, name):
    model_id = model_uri.split("/")[-1]
    download_url = f"https://api.sketchfab.com/v3/models/{model_id}/download"

    headers = {"Authorization": f"Token {SKETCHFAB_API_TOKEN}"}
    response = requests.get(download_url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to get download URL for {name}")
        return None

    download_info = response.json()
    archive_url = download_info.get("gltf", {}).get("url")

    if not archive_url:
        print(f"⚠️ No glTF download available for {name}")
        return None

    print(f"⬇️ Downloading model: {name}")
    zip_response = requests.get(archive_url)
    if zip_response.status_code != 200:
        print("❌ Failed to download ZIP")
        return None

    # Save directly to Unity's Models folder
    output_dir = os.path.join("..", "unity-project", "Assets", "Models", name)
    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(BytesIO(zip_response.content)) as zf:
        zf.extractall(output_dir)

    print(f"✅ Model extracted to {output_dir}")
    return output_dir
