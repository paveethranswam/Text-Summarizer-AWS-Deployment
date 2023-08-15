# To publish package as pypi package or even install as local package
import setuptools
from setuptools import find_packages

# -e installs a project in editable mode (i.e. >setuptools “develop mode”) from a >local project path or a VCS url.

with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "Text-Summarizer-AWS-Deployment"
AUTHOR_NAME = "paveethranswam"
SRC_REPO = "textSummarizer" # SRC Folder name
AUTHOR_EMAIL = "paswam@iu.edu"

# Setuptools.setup will look for constructor file (__init__.py) in every folder in SRC repo and install as local package
setuptools.setup(name = SRC_REPO, 
                 version=__version__,
                 author= AUTHOR_NAME,
                 author_email= AUTHOR_EMAIL,
                 description= long_description,
                 url="https://github.com/{}/{}".format(AUTHOR_NAME, REPO_NAME),
                 project_urls = { "Bug_tracker": "https://github.com/{}/{}/issues".format(AUTHOR_NAME, REPO_NAME)},
                 package_dir={"":"src"},
                 packages= find_packages(where = "src"))

