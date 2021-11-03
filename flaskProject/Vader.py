from flask import Flask, render_template, request, redirect
import tweepy as tp
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

from twitter_auth import *

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

text = 'I hate loving putin'


df = pd.read_csv('Tweets.csv', names=['ID','Text', "pol"])

print (df)

analyser = SentimentIntensityAnalyzer()
blob = TextBlob(text)

tweets = api.search(q='Putin')

print('Textblob output', blob.sentiment.polarity)

list = []

for tweet in tweets:

    sentiment = TextBlob(tweet.text).sentiment.polarity

    if sentiment > 0.15:
        sentiment = 'positive'
    elif sentiment < -.15:
        sentiment = 'neg'
    else:
        sentiment = 'neu'

def sentiment_analyser_score(data):
    score = analyser.polarity_scores(data)
    print("{:-<40} {}".format(data, str(score)))

list = tweets
(list.count('positive', 'negative', 'neutral'))

sentiment_analyser_score(text)

labels = 'Positive', 'negative', 'neutral'
sizes = [sentiment['positive'], sentiment['neg'], sentiment['neu']]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()



