# Components creation
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
import os, sys
from pathlib import Path
import urllib
from textSummarizer.logging import logger
from zipfile import ZipFile
from dataclasses import dataclass
from textSummarizer.entity import DataTransformationConfig
from transformers import pipeline, set_seed
from datasets import load_dataset, load_from_disk, Dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import evaluate
import nltk
import tqdm as tqdm
import torch
nltk.download('punkt')






class DataTransformation:
    def __init__(self, dc : DataTransformationConfig):
        self.dc = dc
        self.tokenizer = AutoTokenizer.from_pretrained(self.dc.model_name)
    
    
    def tokenize_text_batches(self, batch_data):
        input_encodings = self.tokenizer(text = batch_data['dialogue'], padding=True, truncation=True, max_length=1024)
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(text = batch_data['summary'], padding=True, truncation=True, max_length=512)

        # Need to pass target encodings within the dict as labels key for the transformers model input
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }


    def transform_data(self):
        try:
            # Convert text to word encodings using autotokenizer of the pre-trained model
            # dataset = Dataset.from_file(Path(self.dc.data_dir))
            dataset = load_from_disk(Path(self.dc.data_dir))
            data_enc = dataset.map(self.tokenize_text_batches, batched=True, batch_size = 500)
            logger.info('Details about loaded data: {}'.format(data_enc))
            return data_enc
            
        except Exception as e:
            logger.error(e)
            raise e
