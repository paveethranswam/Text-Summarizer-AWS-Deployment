from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.dataIngestion import DataIngestion



class DataIngestionPipeline:
    def main():
        try:
            config = ConfigurationManager()
            dic = config.getDataIngestionConfig()
            di = DataIngestion(dic)

            di.download_data()
            di.extract_zip()
        except Exception as e:
            raise e
        

