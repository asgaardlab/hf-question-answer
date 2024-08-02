# Answering User Questions about Machine Learning Models through Standardized Model Cards

## Install packages
```commandline
pip install -r requirements.txt
```
We used Python 3.11 for this project.

## Prepare Data
### Collect Data
From the `data_collector` directory, run the following command to collect list of models and their discussions from Hugging Face Hub.
```commandline
python main.py
```
* List of models will be created in `data/all_models.csv` file
* Discussions will be saved inside the `data/discussions` directory
  * Discussions from same repository will be saved in a single directory inside the `data/discussions` directory
  * Each discussion will be saved in a single `yaml` file inside it's repository directory 
  * A list of all discussions will be created in `data/all_discussions.csv` file 
### Analyze Sample Data
From the `data_analyzer` directory, run the following command to select sample data.
```commandline
python random_discussion_selector.py
```
* `data/all_random_discussions.csv` file will be created with 378 list of randomly selected discussions.
### Filter Data
From the `data_filter` directory, run the following command to filter the discussions.
```commandline
python main.py
```
* Filtered list of models will be saved in `data/quality_models.csv`
* Discussion list of the filtered models will be saved in `data/quality_models_discussions.csv`
* Filtered list of discussions will be saved in `data/cleaned_discussions.csv` file
### Ground truth for GPT's performance evaluation
* Filter random discussions from `data/all_random_discussions.csv` file running the following command.
```commandline
python random_discussion_cleaner.py
```
* The ground truth we prepared from the filtered random discussions for GPT's performance evaluation is saved in `data/ground_truth.csv`. The ground truth is prepared by manually labeling the discussions.
### Classify Discussion Posts using GPT
From the `discussion_classifier` directory, run the following command to classify the discussion posts.
```commandline
python gpt_classifier.py
```

## Prepare Results
### Generate Plots
### Topic Modeling Discussion Posts
### Result of Manual Question Mapping