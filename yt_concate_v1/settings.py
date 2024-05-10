import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
API_KEY_ORIGINAL = os.getenv("API_KEY")
API_KEY = os.getenv("AK")
print(API_KEY_ORIGINAL)
print(API_KEY)

DOWNLOADS_DIR = "downloads"
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, "videos")
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, "captions")
OUTPUTS_DIR = "outputs"