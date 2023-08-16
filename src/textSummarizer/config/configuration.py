# Configuration manager
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.entity import DataIngestionConfig



@dataclass
class ConfigurationManager:
    config_file_path: Path = CONFIG_FILE_PATH
    params_file_path: Path = PARAMS_FILE_PATH
    
    # Calling this to not override default init and post init is called as the last function of default init
    def __post_init__(self):
        self.config = read_yaml(self.config_file_path) # CONFIG_FILE_PATH taken from constants
        self.params = read_yaml(self.params_file_path) # PARAMS_FILE_PATH taken from constants
        
        create_directories([self.config.artifacts_path, self.config.data_ingestion.root_dir])
        
    def getDataIngestionConfig(self) -> DataIngestionConfig:
        
        data_ingestion_config = self.config.data_ingestion
        
        dic = DataIngestionConfig(root_dir = data_ingestion_config.root_dir, 
                                 source_dir = data_ingestion_config.source_dir, 
                                 local_data_file = data_ingestion_config.local_data_file, 
                                 unzip_dir = data_ingestion_config.unzip_dir)
        
        return dic
    
