import tweepy as tp
from textblob import TextBlob
import pandas as pd


from twitter_auth import *

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)


list = []
tweets = api.search(q="biden", tweet_mode="extended", rpp =100)

for tweet in tweets:
    sentiment = TextBlob(tweet.full_text).sentiment.polarity
    if sentiment > 0.15:
        sentiment = 'positive'
    elif sentiment < -0.15:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    list.append((tweet.full_text, sentiment))

df = pd.DataFrame(list)

print (df)

df.to_csv("Biden.csv", sep=',')

tweets = api.search(q="Trump", tweet_mode="extended", rpp=100)

for tweet in tweets:
    sentiment = TextBlob(tweet.full_text).sentiment.polarity
    if sentiment > 0.15:
        sentiment = 'positive'
    elif sentiment < -0.15:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    list.append((tweet.full_text, sentiment))

df = pd.DataFrame(list)

print (df)

df.to_csv("Trump.csv", sep=',')

tweets = api.search(q="Putin", tweet_mode="extended", rpp=100)

for tweet in tweets:
    sentiment = TextBlob(tweet.full_text).sentiment.polarity
    if sentiment > 0.15:
        sentiment = 'positive'
    elif sentiment < -0.15:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    list.append((tweet.full_text, sentiment))

df = pd.DataFrame(list)

print (df)
df.to_csv("Putin.csv", sep=',')






