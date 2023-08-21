from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.config.configuration import ConfigurationManager
from transformers import pipeline
import torch




class InferencePipeline:
    def __init__(self):
        self.config = ConfigurationManager().getModelEvaluationConfig()

    def inference(self, text):
        tokenizer = self.config.tokenizer_dir
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        pipe = pipeline(task = 'summarization', model = self.config.model_dir, 
                        tokenizer = self.config.tokenizer_dir, device = device, length_penalty = self.config.length_penalty,
                        batch_size = self.config.batch_size)
        
        print('Input Dialogue: ', text)
        print('Summary :', pipe(text)[0]['summary_text'])
        
        return pipe(text)[0]['summary_text']
        












