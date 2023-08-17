from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataValidation import DataValidation

class DataValidationPipeline:
    def main():
        try:
            config = ConfigurationManager()
            dic = config.getDataValidationConfig()
            di = DataValidation(dic)
            di.validate_data()
        
        except Exception as e:
            raise e
