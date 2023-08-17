# Components creation
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
import os, sys
from pathlib import Path
import urllib
from textSummarizer.logging import logger
from zipfile import ZipFile
from dataclasses import dataclass
from textSummarizer.entity import DataValidationConfig




class DataValidation:
    def __init__(self, dic : DataValidationConfig):
        self.dic = dic
    
    def validate_data(self):
        try:
            # Validate files in folder, status is set to true only when all the required files are found
            # Further validation should include column level, handling missing values, row level error fixing
            list_of_files = os.listdir(os.path.join(self.dic.data_dir, 'samsum_dataset'))
            data_validation_status = True

            with open(self.dic.status_dir, 'w') as f:
                f.write('Data validation status: {}'.format(data_validation_status))
            
#             print(self.dic.required_files)
            for req_file in self.dic.required_files:
                if(req_file not in list_of_files):
                    print(req_file)
                    data_validation_status = False
                    with open(self.dic.status_dir, 'w') as f:
                        f.write('Data validation status: {}'.format(data_validation_status))

                logger.info('Data Validation status: {}'.format(data_validation_status))
                return data_validation_status
            
            logger.info('Data Validation status: {}'.format(data_validation_status))
            
        except Exception as e:
            logger.error(e)
            raise e
    