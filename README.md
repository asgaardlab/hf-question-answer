# Answering User Questions about Machine Learning Models through Standardized Model Cards
## Install packages
```commandline
pip install -r requirements.txt
```
We used Python 3.11 for this project.
## Collect Data
From the `data_collector` directory, run the following command to collect list of models and their discussions from Hugging Face Hub.
```commandline
python main.py
```
The list of models will be saved in `all_models.csv` and the discussions will be saved inside the `data/discussions` directory.
## Sample Data Analysis
### Ground truth for GPT's performance evaluation
## Filter Data
## Classify Data using GPT
## Generate Plots