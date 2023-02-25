# PSG sleep stage classification
![alttext](https://github.com/parksu111/psg-classification/blob/main/img/psg.png)


## Introduction
This competition task was developed as part of an educational program hosted by [KOSMES](https://www.kosmes.or.kr/sbc/SH/EHP/SHEHP001M0.do) and run by [MNC](https://mnc.ai/). The actual competition page can be found [here](https://aiconnect.kr/competition/detail/209/task/238/taskInfo). 

This repository contains the code that went into the preparation of an AI competition task. This inlcudes:
* Processing raw data.
* Training a baseline model.
* Preparing code to evaluate user predictions.

## Competition Task Overview
* Description: Classify sleep stages in humans (Wake, N1, N2, N3, REM) using PSG(polysomnography) signals.
* Data: 90 second PSG signals saved in .npy format.
* Evaluation: Macro F1-Score
    * The public leaderboard is calculated using 30% of the test data. The final leaderboard is calculated using the entire test set.

## Raw Data
The raw data used for this project can be downloaded [here](https://sleepdata.org/). Some sample data can be downloaded [here](https://drive.google.com/drive/folders/1x79gC2nfG_Jf7cuFxJBbho4U2j5Pt3sd?usp=sharing). The raw dataset consists of:
* .edf (European Data Format) files containing PSG recordings.
* .tsv files containing labels of sleep-related events.

## Competition Preparation
* This [notebook](https://github.com/parksu111/psg-classification/blob/main/data_prep.ipynb) contains EDA of the raw data along with a detailed explanation of the steps taken to process the raw data into data ready for a competition.
* This [notebook](https://github.com/parksu111/psg-classification/blob/main/evaluation_prep.ipynb) details the steps to prepare files/code used for evaluating user submissions.
* This [notebook](https://github.com/parksu111/psg-classification/blob/main/baseline.ipynb) contains the baseline model provided to participants.

## Baseline Model
The baseline model uses two 1-d CNNs. It is based on DeepSleepNet which can be found in this [paper](https://arxiv.org/abs/1703.04046).
![alttext](https://github.com/parksu111/psg-classification/blob/main/img/baseline_architecture.png)

## Files
* *data_prep.ipynb* - Jupyter Notebook detailing how the raw data was processed to make the train and test datasets used for the competition.
* *evaluation_prep.ipynb* - Jupter Notebook detailing preparation of evaluation of user submissions.
* *baseline.ipynb* Jupyter Notebook of the baselie model for this task.
    * Includes both the training and inference steps.
    * Same notebook is also available in Korean.
* preprocess/
    * *make_npy.py* - Script to extract signals from edf files and save as .py files.
    * *label_split_npy.py* - Script to extract sleep stages from tsv files and prepare train / test .py files.
    * *split_data.py* - Script to split entire dataset into train and test datasets.
* utils/
    * *normalize.py* - Script to extract mean and standard deviation of raw signals.
* evaluate/
    * *answer.csv* - CSV file containing the labels of the test data
    * *sample_submission.csv* - Sample CSV file that competition participants can use to prepare their prediction files.
    * *evaluate.py* - Script to load participant predictions and calculate performance.

