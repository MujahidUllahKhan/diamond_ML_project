from src.components.data_ingestion import DataIngestion
from src.logger import get_logger

logger = get_logger(__name__)

class TrainingPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        logger.info("Training pipeline started")
        obj = DataIngestion()
        obj.initiate_data_ingestion()
        logger.info("Training pipeline completed")