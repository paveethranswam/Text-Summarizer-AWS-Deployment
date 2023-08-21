# Configuration manager
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig



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



    def getDataTransformationConfig(self) -> DataTransformationConfig:

        data_transformation_config = self.config.data_transformation

        create_directories([data_transformation_config.root_dir])

        dc = DataTransformationConfig(root_dir = Path(data_transformation_config.root_dir), 
                                   data_dir = Path(data_transformation_config.data_dir),
                                 model_name = str(data_transformation_config.model_name))

        return dc




    def getModelTrainerConfig(self) -> ModelTrainerConfig:
        
        # Take model name from config file
        # Take other training arguments from params file
        
        model_trainer_params = self.params.TrainingArguments  
        create_directories([Path(model_trainer_params.output_dir)])
        
        mtc = ModelTrainerConfig(model_name = self.config.model_trainer.model_name,
                                  output_dir= Path(model_trainer_params.output_dir),
                                  num_train_epochs= int(model_trainer_params.num_train_epochs),
                                  warmup_steps = model_trainer_params.warmup_steps,
                                  per_device_train_batch_size= model_trainer_params.per_device_train_batch_size,
                                  per_device_eval_batch_size= model_trainer_params.per_device_eval_batch_size,
                                  weight_decay= model_trainer_params.weight_decay,
                                  logging_steps= model_trainer_params.logging_steps,
                                  gradient_accumulation_steps= model_trainer_params.gradient_accumulation_steps,
                                  evaluation_strategy = model_trainer_params.evaluation_strategy,
                                  predict_with_generate= model_trainer_params.predict_with_generate)
        
        return mtc
    


    def getModelEvaluationConfig(self) -> ModelEvaluationConfig:
        
        # Take model name from config file
        # Take other training arguments from params file
        
        model_eval_config = self.config.model_evaluation  
        
        mec = ModelEvaluationConfig(
                                model_name = model_eval_config.model_name,
                                data_dir = Path(model_eval_config.data_dir),
                                model_dir = model_eval_config.model_dir,
                                tokenizer_dir = model_eval_config.tokenizer_dir,
                                length_penalty = model_eval_config.length_penalty,
                                max_length = model_eval_config.max_length,
                                batch_size = model_eval_config.batch_size)
        
        return mec