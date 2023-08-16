# Components creation
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
import os, sys
from pathlib import Path
import urllib
from textSummarizer.logging import logger
from zipfile import ZipFile
from dataclasses import dataclass
from textSummarizer.entity import DataIngestionConfig




class DataIngestion:
    def __init__(self, dic : DataIngestionConfig):
        self.dic = dic
        
    # Download the data from url and save to the local file name and extract the zip contents, save them all in artifacts folder
    def download_data(self):
        if(not os.path.exists(self.dic.local_data_file)):
            filename, header = urllib.request.urlretrieve(url = self.dic.source_dir, filename = self.dic.local_data_file)
            logger.info('Data file {} downloaded, with return header {}'.format(filename, header))
        else:
            size = get_size(Path(self.dic.local_data_file))
            logger.info('Data file {} already exists, with {}'.format(self.dic.local_data_file, size))
    # Extract
    def extract_zip(self):
        with ZipFile(self.dic.local_data_file, 'r') as zObject:
            zObject.extractall(path=self.dic.unzip_dir)
        logger.info('Zip file extracted at {}'.format(self.dic.unzip_dir))



