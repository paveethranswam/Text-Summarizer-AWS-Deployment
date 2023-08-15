import os
from pathlib import Path # Handles filenames with proper slashes specific to every os and give correct filename paths
import logging

logging.basicConfig(level = logging.INFO, format='[%(asctime)s] @ [%(levelname)s] : %(message)s', )

# 1. To install this project as a package in python, we need to package the code as a py file. And to do this, we need to specify 
# import instructions in __init__.py file. Other packages are components and utils.

# 2. Build a docker image of the source code and deploy the image in EC2 machine of AWS

# 3. Research will contain all the notebook experiments
project_name = 'textSummarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create files in file directory if file directory is empty
    if( filedir ):
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory {} for file {}".format(filedir, filename))

    if( (not os.path.exists(filepath) ) or (os.path.getsize(filepath) == 0) ):
        f = open(filepath, "w")
        logging.info('Creating empty file {}'.format(filepath))

    else:
        logging.info('File {} already exists'.format(filepath))
