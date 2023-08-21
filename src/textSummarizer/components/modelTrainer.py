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
from textSummarizer.entity import ModelTrainerConfig
from pathlib import Path
import os
from textSummarizer.logging import logger
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size





class ModelTrainer:
    def __init__(self, mtc : ModelTrainerConfig):
        self.mtc = mtc
        self.tokenizer = AutoTokenizer.from_pretrained(self.mtc.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.mtc.model_name)
        self.metric = evaluate.load('rouge')
    
    
    # Define metric
    def compute_metrics(self, predictions):
        # To decode the generated tokens to words
        preds, labels = predictions
        
        labels = np.where(labels != -100, labels, self.tokenizer.pad_token_id)
        decoded_preds = self.tokenizer.batch_decode(preds, skip_special_tokens=True, clean_up_tokenization_spaces = True)
        decoded_labels = self.tokenizer.batch_decode(labels, skip_special_tokens=True, clean_up_tokenization_spaces = True)
        
        # rougeLSum expects newline after each sentence
        decoded_preds = ["\n".join(nltk.sent_tokenize(pred.strip())) for pred in decoded_preds]
        decoded_labels = ["\n".join(nltk.sent_tokenize(label.strip())) for label in decoded_labels]

#         prediction_summary = [self.tokenizer.decode(token, skip_special_tokens=True, clean_up_tokenization_spaces = True) 
#                              for token in predictions]
        
        # Compute ROUGE score
        return self.metric.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
    
    
    def train_model(self, data_transformed):
        
        training_args = Seq2SeqTrainingArguments(output_dir = self.mtc.output_dir, 
                                          num_train_epochs = self.mtc.num_train_epochs,
                                          warmup_steps = self.mtc.warmup_steps, 
                                          per_device_train_batch_size = self.mtc.per_device_train_batch_size,
                                          per_device_eval_batch_size = self.mtc.per_device_eval_batch_size,
                                          weight_decay = self.mtc.weight_decay,
                                          logging_steps = self.mtc.logging_steps,
                                          gradient_accumulation_steps= self.mtc.gradient_accumulation_steps,
                                          evaluation_strategy = self.mtc.evaluation_strategy,
                                          predict_with_generate= self.mtc.predict_with_generate)

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # Data collators are objects that will form a batch by using a list of dataset elements as input.
        # These elements are of the same type as the elements of train_dataset or eval_dataset. 
        # To be able to build batches, data collators may apply some processing (like padding).
        # Some of them (like DataCollatorForLanguageModeling) also apply some random data augmentation 
        # (like random masking) on the formed batch.
        
        seq2seq_dc = DataCollatorForSeq2Seq(tokenizer=self.tokenizer, model = self.model)

        trainer = Trainer(model = self.model.to(device), args = training_args, tokenizer = self.tokenizer,
                          data_collator = seq2seq_dc, train_dataset = data_transformed['test'], 
                          eval_dataset = data_transformed['validation'], compute_metrics = self.compute_metrics)
        
        # trainer.train()

        ## Save model after fine-tuning
        self.model.save_pretrained(Path(self.mtc.output_dir))
    
        ## Save tokenizer after making it train on the fine tune dataset
        self.tokenizer.save_pretrained(os.path.join(self.mtc.output_dir, 'tokenizer'))

        logger.info('Model trained and model files saved to {}'.format(self.mtc.output_dir))
    