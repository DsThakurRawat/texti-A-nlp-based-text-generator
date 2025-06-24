class ConfigurationManager:
    def __init__(self):
        pass  # Add your configuration logic here

    def get_data_ingestion_config(self):
        from textsummarizer.entity import DataIngestionConfig
        return DataIngestionConfig(
            source_url="https://github.com/DsThakurRawat/DsThakurRawat-AIML-IN-PRODUCTION-1-Texti/raw/refs/heads/main/summarizer-data.zip",  # <-- Use a real URL here!
            local_data_file="data/data.zip",            # <-- Use a valid path
            unzip_dir="data/unzipped"                   # <-- Use a valid path
        )