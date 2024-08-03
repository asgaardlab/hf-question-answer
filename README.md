# Answering User Questions about Machine Learning Models through Standardized Model Cards


## Install packages
```commandline
pip install -r requirements.txt
```
We used Python 3.11 for this project.


## Prepare Data

### Collect Data
To collect list of models and their discussions from Hugging Face Hub, run the following command from the `data_collector` directory.
```commandline
python main.py
```
* List of models will be saved in `data/all_models.csv` file
* Discussions along with pull requests will be saved inside the `data/discussions` directory. The directory structure is as followed:
```
├── data: all the data generated after running the scripts are saved in this directory
│   ├── discussions: directory to save all discussions and pull requests
│   │   ├── <model_id>: model repository to save discussions and pull requests. the `/` in the `model_id` is replaced with '@'. an empty directory means there are no discussions and pull requests in the repository.
│   │   │   ├── discussion_<discussion_number>.yaml: a discussion file containing the discussion details
│   │   │   ├── pull_request_<pull_request_number>.yaml: a pull request file containing the pull request details
```
* A list of the downloaded discussions will be created in `data/all_discussions.csv` file 

### Analyze Sample Data
To select sample data for manual analysis, run the following command from the `data_analyzer` directory.
```commandline
python random_discussion_selector.py
```
* 378 list of randomly selected discussions will be created in `data/all_random_discussions.csv` file 

### Filter Data
To filter the random discussions in `data/all_random_discussions.csv` file, run the following command from `data_filter` directory.
```commandline
python random_discussion_cleaner.py
```
To filter all the discussions, run the following command from the `data_cleaner` directory.
```commandline
python main.py
```
* Filtered list of models will be saved in `data/quality_models.csv`
* Discussion list of the filtered models will be saved in `data/quality_models_discussions.csv`
* Filtered list of discussions will be saved in `data/cleaned_discussions.csv` file

### Ground truth for GPT's performance evaluation
* The ground truth we prepared from the filtered random discussions for GPT's performance evaluation is saved in `data/ground_truth.csv`. The ground truth is prepared by manually labeling the discussions.

### Classify Discussion Posts using GPT
To classify the filtered random discussion posts using `gpt-3.5-turbo-0125`, run the following command from the `discussion_classifier` directory
```commandline
python random_discussion_classifier.py
```
To classify all the filtered discussion posts using `gpt-3.5-turbo-0125`, run the following command from the `discussion_classifier` directory 
```commandline
python all_discussion_classifier.py
```
* Classification result will be saved in columns of `data/.csv` file
* A list of all question-containing discussions will be created in `data/.csv` file 

### Evaluate GPT's Performance
The performance evaluation of GPT in classifying the random discussion posts as question-containing post is available in `data/gpt_performance_evaluation.csv` file.


## Prepare Results

### Generate Plots
To generate all the plots, run the following command from the `plot_generator` directory  
```commandline
python main.py
```
* Plots will be saved in `data/plots` directory

### Topic Modeling Discussion Posts
To train a BERTopic model on the discussion posts, run the following command from the `discussion_topic_modeller` directory 
```commandline
python bertopic_topic_modeller.py
```
* The trained BERTopic model will be saved in `data/bertopic_model/...` directory
* To visualize the topics, run the `bertopic_topic_visualizer.ipynb` notebook. 

To cluster the topics, run the `bertopic_topic_clusterer.ipynb` notebook.

### Result of Manual Question Mapping
The result of manual question mapping is saved in `data/manual_question_mapping.csv` file.
To calculate the inter-rater agreement, run the following command from the `data_analyzer` directory
```commandline
python irr_calculator.py
```