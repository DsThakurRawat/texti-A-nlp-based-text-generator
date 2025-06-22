import os 
import box.exceptions import BoxValueError
import yaml
from textsummarizer.logging._init_ import logger
from ensure import ensure_annotations
from box import configBox
from pathlib import Path
from typing import any


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """reads yaml file and returns
    args:
        path_to_yaml (str): path like input
    Raises:
          ValueError: if yaml file is empty
          e: empty file
    Returns:
      configBox: ConfigBox type
    
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return configBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e