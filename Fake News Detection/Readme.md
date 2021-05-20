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

### Working Process
1) Cleaning of Data
  - Lower Casing
  - Removing Punctuations
  - Removing stopwords
2) Train Test Splitting the Dataset
3) Feature Extraction using CountVectorizer function
4) Model Used: LogisticRegression
5) Metrics Used: ROC_AUC_SCORE
6) Ploting of Confusion Matrix to check resuls

### Model Training and Testing
The model was trained and tested for three different features separately
  - Title
  - Text
  - Title + Text

### Model Performance
For all the three training and testing the scores were as follows
1) For Title only ![Screenshot (104)](https://user-images.githubusercontent.com/69076815/118935247-f5697a80-b968-11eb-8305-b65f1090279d.png)
2) 














