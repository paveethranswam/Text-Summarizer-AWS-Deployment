from transformers import pipeline, set_seed
from datasets import load_dataset, load_from_disk, Dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
from transformers import TrainingArguments, Seq2SeqTrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq            
import evaluate
import nltk
import tqdm as tqdm
import torch
nltk.download('punkt')
from textSummarizer.entity import ModelEvaluationConfig
from pathlib import Path
import os
from textSummarizer.logging import logger
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size






class ModelEvaluation:
    def __init__(self, mec : ModelEvaluationConfig):
        self.mec = mec
        self.tokenizer = AutoTokenizer.from_pretrained(self.mec.tokenizer_dir) # Load tokenizer from path not model name
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.mec.model_dir)  # Load model from path not model name
        self.metric = evaluate.load('rouge')
    
    def eval_model(self):
        dataset = load_from_disk(self.mec.data_dir)['validation'][:10]

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        content_data = []
        target_data = []
#         print(dataset)
        
        for i in range(0, len(dataset['id']), self.mec.batch_size):
            content_data.append(dataset['dialogue'][i: i+self.mec.batch_size])
            target_data.append(dataset['summary'][i: i+self.mec.batch_size])

        for content, target in tqdm.tqdm(zip(content_data, target_data), total = len(content_data)):
            content_enc = self.tokenizer(text = content, padding=True, truncation=True, max_length=1024, return_tensors = 'pt')
                
            prediction_tokens = self.model.generate(input_ids = content_enc['input_ids'].to(device),
                                           attention_mask = content_enc['attention_mask'].to(device),
                                           length_penalty = self.mec.length_penalty, max_length = self.mec.max_length)
            
            
            # To decode the generated tokens to words
            prediction_summary = [self.tokenizer.decode(token, skip_special_tokens=True, clean_up_tokenization_spaces = True) 
                                 for token in prediction_tokens]
            
         
            print('origg preds: ', prediction_summary, '\n')
            print('orig labels: ',target, '\n')
            
            # rougeLSum expects newline after each sentence
            decoded_preds = ["\n".join(nltk.sent_tokenize(pred.strip())) for pred in prediction_summary]
            decoded_labels = ["\n".join(nltk.sent_tokenize(label.strip())) for label in target]
            
            print('decoded preds: ', decoded_preds, '\n')
            print('decoded_labels: ',decoded_labels, '\n')
            
            # Compute ROUGE score
            self.metric.add_batch(predictions = decoded_preds, references= decoded_labels)
            
        result = self.metric.compute(use_stemmer=True)
        return result
            



