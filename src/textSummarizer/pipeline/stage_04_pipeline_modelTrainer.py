from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.modelTrainer import ModelTrainer



class ModelTrainerPipeline:
    def main(data_transformed):
        try:
            config = ConfigurationManager()
            dc = config.getModelTrainerConfig()
            di = ModelTrainer(dc)
            di.train_model(data_transformed)
            
        except Exception as e:
            raise e

