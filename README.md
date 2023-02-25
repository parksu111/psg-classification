# PSG sleep stage classification

## Introduction
This competition task was developed as part of an educational program hosted by [KOSMES](https://www.kosmes.or.kr/sbc/SH/EHP/SHEHP001M0.do) and run by [MNC](https://mnc.ai/). The actual commpetition page can be found [here](https://aiconnect.kr/competition/detail/209/task/238/taskInfo). 

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
The raw data used for this project can be downloaded [here](https://sleepdata.org/). Some sample data can be downloaded [here](). The raw dataset consists of:
* .edf (European Data Format) files containing PSG recordings.
* .tsv files containing labels of sleep-related events.

## Competition Preparation
* This [notebook]() contains EDA of the raw data along with a detailed explanation of the steps taken to process the raw data into data ready for a competition.
* This [notebook]() details the steps to prepare files/code used for evaluating user submissions.
* This [notebook]() contains the baseline model provided to participants.

## Baseline Model
The baseline model uses two 1-d CNNs. It is based on DeepSleepNet which can be found in this [paper](https://arxiv.org/abs/1703.04046).

## Files
