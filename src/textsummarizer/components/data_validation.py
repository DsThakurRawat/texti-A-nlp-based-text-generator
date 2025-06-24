import os 
from textsummarizer.logging.logger import logger
from textsummarizer.entity import DataIngestionConfig
from textsummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config : DataValidationConfig):
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    logger.error(f"Missing required file: {file}")
                else:
                    validation_status = True