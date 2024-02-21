from pathlib import Path
import os

PARENT_DIR = Path(__file__).parent.resolve().parent
RAW_DATA_DIR = PARENT_DIR / 'data'
TRANSFORMED_DATA_DIR = RAW_DATA_DIR / 'transformed'
