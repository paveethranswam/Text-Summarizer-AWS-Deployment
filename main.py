from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataIngestion import DataIngestion
from textSummarizer.pipeline.stage_01_pipeline_dataIngestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info("\n\n >>>>>>>>>> Stage {} started <<<<<<<<<< ".format(STAGE_NAME))
    DataIngestionPipeline.main()
    logger.info(">>>>>>>>>> Stage {} complete <<<<<<<<<< \n\n".format(STAGE_NAME))

except Exception as e:
    logger.error(e)
    raise e








