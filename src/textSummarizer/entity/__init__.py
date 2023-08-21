import os, sys
from pathlib import Path
import urllib
from textSummarizer.logging import logger
from zipfile import ZipFile
import numpy as np
from dataclasses import dataclass



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_dir: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    status_dir: str
    required_files: list



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    model_name: str



@dataclass(frozen=True)
class ModelTrainerConfig:
    model_name: str
    output_dir: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    gradient_accumulation_steps: int
    evaluation_strategy: str
    predict_with_generate: bool



@dataclass(frozen=True)
class ModelEvaluationConfig:
    model_name: str
    data_dir: Path
    model_dir: Path
    tokenizer_dir: Path
    length_penalty: float
    max_length: int
    batch_size: int

    
