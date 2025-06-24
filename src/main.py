from textsummarizer.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline

from textsummarizer.logging.logger import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
except Exception as e:
    logger.exception(f">>>>>>>>>> stage {STAGE_NAME} failed <<<<<<<<")
    raise e