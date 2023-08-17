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




    