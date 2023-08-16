# Text Summarization with deployement in AWS EC2 Machine and CI/CD with github actions

#### Enusre annotations will make sure your functions throws an error when non-matching data type is given as input.
#### If a function f(x: int, y: int): x*y abd we call f(x=2, y='4'), the output x*y is 2*'4'= '44'. So adding ensure annotations will 
#### give an error

#### ConfigBox is a custom dictionary, where we can access d['keys_1'] as d.keys_1, which would not work in normal dict type.
#### Better. This is better to have than normal dict type.

#### Read about Data Classes, how they are different from normal classes and named tuple. And we can mention in we need to freeze the values
#### of the class from changing or allow them to change dynamically. https://realpython.com/python-data-classes/

1. Update config.yaml
2. Update params.yaml and update constants
3. Update entity.yaml - Entity is the return type of a function
4. Update configuration manager in src/textSummarizer/config - It reads the configuration data from an external YAML or JSON file and it injects this data into the application
5. Update the components in src/textSummarizer/components (Data ingestion and Data monitoring)
6. Update the pipeline in src/textSummarizer/pipeline
7. Update main.py
8. Update app.py


