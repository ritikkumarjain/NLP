To look at bertopic plots look into this notebook: [Notebook](https://www.kaggle.com/ritikjain00/topic-modelling-of-climate-disasters/notebook)

# Topic Modelling of Climate disasters

### Project Status ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
- Finding Insights: Completed
- Paper Writing: In Progress

### Introduction ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
With the rise of social media in recent years, it has become a valuable research tool for people's opinions on a variety of topics. When it comes to climate change, there are a few concerns to consider.
- What are people doing to cope with extreme weather and climate change?
- Is it possible that people adapt without even realizing it?

The study's significance was to learn how Natural Language Processing methodologies could be used to assess user sentiments in response to extreme weather events.

Through this study we tested the usability of a popular social media tool i.e., Twitter as a possible disaster response tool.

### Table of Contents ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
1) [Motivation](###Motivation)
2) [Objectives](###Objectives)
3) [Selected Climate Event](###Selected-Climat-Event)
4) [Data Collection](Data Collection)
5) [Methods](Methods)
6) [Results](Results)


### 1) Motivation ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
The main motivation behind our study was to use Twitter to capture public awareness of climate change

### 2) Objectives ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
The overarching objective of this research is to study and evaluate dynamics of climate events tweets around selected climatic events.
This specific objectives are: 
- Collect and preprocess twitter feeds using data mining techniques.
- Apply different types of Natural Language Processing techniques i.e., Topic Modelling to study the data.
- Evaluate effectiveness of different predictive modelling techniques on the data
- Characterize tweets dynamics to compare the climatic events discussion in the event zone.

### 3) Climate Event - Amphan Cyclone ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
Amphan Cyclone is a category 5 cyclone which hit India's eastern coast in May 2020. It was one of the most powerful storm in the Bay of Bengal.

Some Reasons for choosing this events was:
- 4.4 million people were affected
- Countries impacted: India and Bangladesh 
- Estimated economic loss: 13.7 billion dollars
- Ecosystem scale damage: 
  - Agricultural lands (78.25%)
  - Forest, including mangroves (10.8%) 

### 4) Data Collection ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
Snscrape is a open source python tool which was used collect tweets from twitter.
- The “Amphan” hashtag to extract tweets content.
- Other things like userid, datetime of tweet,user name, reply_count, retweet_count, like_count, quote_count were also extracted
- A total of 134,300 tweets were extracted. 
- After Cleaning, around 40,000 tweets remained.

### 5) Models used ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)
- LDA
- NNMF
- BERTopic(Transformer models)

### 6) Results ![image](https://user-images.githubusercontent.com/69076815/148382182-c43da7f7-6f46-4562-9d6e-db3aa9deb700.png)








