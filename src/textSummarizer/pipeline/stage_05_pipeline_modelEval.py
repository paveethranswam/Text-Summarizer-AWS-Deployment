from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories, get_size
from pathlib import Path
from textSummarizer.logging import logger
from dataclasses import dataclass
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.modelEvaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def main():
        try:
            config = ConfigurationManager()
            dc = config.getModelEvaluationConfig()
            me = ModelEvaluation(dc)
            rouge_score = me.eval_model()
            logger.info('Evaluation ROUGE Score: {} '.format(rouge_score))
            
        except Exception as e:
            raise e

