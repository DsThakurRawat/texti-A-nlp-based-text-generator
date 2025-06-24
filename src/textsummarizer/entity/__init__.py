# filepath: src/textsummarizer/entity/__init__.py

from .data_ingestion_config import DataIngestionConfig

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path




@dataclass(frozen=True) 
class DataValidationconfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    

