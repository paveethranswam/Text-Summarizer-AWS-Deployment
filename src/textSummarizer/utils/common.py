import os
import yaml
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# Enusre annotations will make sure your functions throws an error when non-matching data type is given as input.
# If a function f(x: int, y: int): x*y abd we call f(x=2, y='4'), the output x*y is 2*'4'= '44'. So adding ensure annotations will 
# give an error

# ConfigBox is a custom dictionary, where we can access d['keys_1'] as d.keys_1, which would not work in normal dict type.
# Better. This is better to have than normal dict type.

@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    # Reads a yaml file and returns a config box object
    try:
        with open(yaml_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info('Path to YAML {} loaded correctly'.format(yaml_path))
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file {} is empty".format(yaml_path))
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(directory_path: list):
    # Create a list of directories. Directories will be created and removed dynamically while running the program
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        logger.info("Directory {} created correctly".format(path))


@ensure_annotations
def get_size(file_path: Path):
    return "File size: {} kB".format(os.path.getsize(file_path)/1024)




