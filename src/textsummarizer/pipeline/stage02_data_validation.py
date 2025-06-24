from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.logging.logger import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataValidation(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    