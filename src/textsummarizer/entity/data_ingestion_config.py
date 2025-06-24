# filepath: src/textsummarizer/entity/data_ingestion_config.py
class DataIngestionConfig:
    def __init__(self, source_url: str, local_data_file: str, unzip_dir: str):
        self.source_url = source_url
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir