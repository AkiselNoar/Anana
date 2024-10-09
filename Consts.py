import os
from pathlib import Path

DROPBOX = Path(os.environ["HOME"], "Dropbox")
HTA_PATH = DROPBOX / "Listings"

if not HTA_PATH.exists():
    HTA_PATH.mkdir(exist_ok=True, parents=True)
