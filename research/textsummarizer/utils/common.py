import os
import yaml
from pathlib import Path
from typing import Any, List

from box import Box
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from textsummarizer.logging.logger import logger

# Utility functions

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """Reads a YAML file and returns its contents as a Box (dot-access dict)."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return Box(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

def create_directories(paths: List[Path], verbose: bool = True):
    """Creates multiple directories if they don't exist."""
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file/folder in a human-readable format."""
    total_size = 0
    if path.is_file():
        total_size = path.stat().st_size
    elif path.is_dir():
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
    size_in_kb = round(total_size / 1024, 2)
    return f"~ {size_in_kb} KB"