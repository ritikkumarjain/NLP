# Fake News Detection
---
### Description

The Repo contains ML model to classify whether news is Fake or Not Fake from 6 different categories.
1) News
2) Politics
3) Left-News
4) Government-News
5) US_News
6) Middle-East

### Dataset
The dataset can be downloaded from Kaggle.
Link: https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset
The Dataset Contains two files: Fake.csv(Containing only fake news) and True.csv(Containing only true news)
Both the Datasets were combined to form a single dataset
The Combined Dataset have following Features:
  - Title
  - Text
  - Subject
  - Date
  - Target(Fake=1,True=0)

## Approach 1:
1) Data Processing and Logistic Regression used to classify news
2) Achieve Accuracy of 0.97

## Approach 2
1) Using LSTM

## Approach 3
1)
2) Also Predicitions were made on basis on Number of punctuations in senetences and length of sentences.
3) Model achieve a decent F1 score of 0.93.



