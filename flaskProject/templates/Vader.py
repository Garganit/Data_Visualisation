import tweepy as tp
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from textblob import TextBlob


from twitter_auth import *

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tp.API(auth)

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


        sentiment_analyser_score(text)


