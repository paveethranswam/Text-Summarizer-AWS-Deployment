# Configuration manager
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig



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
        
        dic = DataIngestionConfig(root_dir = Path(data_ingestion_config.root_dir), 
                                 source_dir = str(data_ingestion_config.source_dir), 
                                 local_data_file = Path(data_ingestion_config.local_data_file), 
                                 unzip_dir = Path(data_ingestion_config.unzip_dir))
        
        return dic
    


    def getDataValidationConfig(self) -> DataValidationConfig:
        
        data_validation_config = self.config.data_validation  
        create_directories([data_validation_config.root_dir])
        
        dic = DataValidationConfig(root_dir = Path(data_validation_config.root_dir), 
                                   data_dir = Path(data_validation_config.data_dir),
                                 status_dir = str(data_validation_config.status_dir), 
                                 required_files = data_validation_config.required_files)
        
        return dic





