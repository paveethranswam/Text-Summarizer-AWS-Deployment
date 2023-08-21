from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataTransformation import DataTransformation



class DataTransformationPipeline:
    def main():
        try:
            config = ConfigurationManager()
            dc = config.getDataTransformationConfig()
            di = DataTransformation(dc)
            data_transformed = di.transform_data()
            return data_transformed
        
        except Exception as e:
            raise e

