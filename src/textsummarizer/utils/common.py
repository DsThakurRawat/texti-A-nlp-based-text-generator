import os
import yaml
from pathlib import Path
from typing import Any

from box import Box, BoxValueError
from ensure import ensure_annotations
from textsummarizer.logging import logger  # Make sure your __init__.py is spelled correctly
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """Reads a YAML file and returns its contents as a Box (dot-access dict).

    Args:
        path_to_yaml (Path): Path to the YAML file

    Raises:
        ValueError: If the YAML file is empty
        Exception: For other exceptions

    Returns:
        Box: Parsed YAML content with dot notation access
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return Box(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
