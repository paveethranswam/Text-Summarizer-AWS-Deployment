# Text Summarization with deployement in AWS EC2 Machine and CI/CD with github actions

#### Enusre annotations will make sure your functions throws an error when non-matching data type is given as input. If a function f(x: int, y: int): x*y abd we call f(x=2, y='4'), the output x*y is 2*'4'= '44'. So adding ensure annotations will  give an error.

#### ConfigBox is a custom dictionary, where we can access d['keys_1'] as d.keys_1, which would not work in normal dict type. Better. This is better to have than normal dict type.

#### Read about Data Classes, how they are different from normal classes and named tuple. And we can mention in we need to freeze the values of the class from changing or allow them to change dynamically. https://realpython.com/python-data-classes/

#### Unsolved mysteries: import urllib and import urllib.request both are needed. Don't know why this has to be done but without importing this, the code does not work.


### Improvements to do:
#### 1. In data validation stage, Validate files in folder, status is set to true only when all the required files are found. Further validation should include column level, data type checking - extract scheme information using glue crawler and store the metadata in the AWS Glue Data Catalog, handling missing values, row level error fixing.

#### 2. In model training stage, use Huggingface with sagemaker estimator and deploy endpoint to run on sagemaker instance. https://huggingface.co/docs/sagemaker/train


1. Update config.yaml
2. Update params.yaml and update constants
3. Update entity.yaml - Entity is the return type of a function
4. Update configuration manager in src/textSummarizer/config - It reads the configuration data from an external YAML or JSON file and it injects this data into the application
5. Update the components in src/textSummarizer/components (Data ingestion and Data monitoring)
6. Update the pipeline in src/textSummarizer/pipeline
7. Update main.py
8. Update app.py



Steps to do deployment:
1. Connect to EC2 machine: A virtual machine to run docker containers
2. Connect ECR: Elastic Container Registry to save docker image in aws

3. Build docker image of source code
4. Push docker image to ECR
5. Launch EC2 machine
6. Pull image from ECR to EC2 machine
7. Launch docker image in EC2

# Policy:
- Amazon EC2 full access
- Amazon EC2 Container Registry (ECR) full access

