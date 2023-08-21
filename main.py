from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataIngestion import DataIngestion
from textSummarizer.pipeline.stage_01_pipeline_dataIngestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_pipeline_dataValidation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_pipeline_dataTransformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_pipeline_modelTrainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_pipeline_modelEval import ModelEvaluationPipeline

def begin_main():
    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info("\n\n >>>>>>>>>> Stage {} started <<<<<<<<<< ".format(STAGE_NAME))
        DataIngestionPipeline.main()
        logger.info(">>>>>>>>>> Stage {} complete <<<<<<<<<< \n\n".format(STAGE_NAME))
        
    except Exception as e:
        logger.error(e)
        raise e






    STAGE_NAME = "Data Validation Stage"
    try:
        logger.info("\n\n >>>>>>>>>> Stage {} started <<<<<<<<<< ".format(STAGE_NAME))
        DataValidationPipeline.main()
        logger.info(">>>>>>>>>> Stage {} complete <<<<<<<<<< \n\n".format(STAGE_NAME))

    except Exception as e:
        logger.error(e)
        raise e







    STAGE_NAME = "Data Transformation Stage"
    try:
        logger.info("\n\n >>>>>>>>>> Stage {} started <<<<<<<<<< ".format(STAGE_NAME))
        data_transformed = DataTransformationPipeline.main()
        logger.info(">>>>>>>>>> Stage {} complete <<<<<<<<<< \n\n".format(STAGE_NAME))

    except Exception as e:
        logger.error(e)
        raise e






    STAGE_NAME = "Model Training and Fine Tuning Stage"
    try:
        logger.info("\n\n >>>>>>>>>> Stage {} started <<<<<<<<<< ".format(STAGE_NAME))
        ModelTrainerPipeline.main(data_transformed)
        logger.info(">>>>>>>>>> Stage {} complete <<<<<<<<<< \n\n".format(STAGE_NAME))

    except Exception as e:
        logger.error(e)
        raise e





    STAGE_NAME = "Model Evaluation on Validation data Stage"
    try:
        logger.info("\n\n >>>>>>>>>> Stage {} started <<<<<<<<<< ".format(STAGE_NAME))
        ModelEvaluationPipeline.main()
        logger.info(">>>>>>>>>> Stage {} complete <<<<<<<<<< \n\n".format(STAGE_NAME))

    except Exception as e:
        logger.error(e)
        raise e
    























