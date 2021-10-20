from flask import Flask, render_template, request, redirect

import tweepy as tp
from textblob import TextBlob


from twitter_auth import *

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

app = Flask(__name__)

@app.route('/part3', methods=['GET'])
def part3():
    return render_template('part3.html')

@app.route('/part4', methods=['GET'])
def part4():
    return render_template('part4.html')

@app.route('/tweets', methods=['POST', 'GET'])
def tweetspage():  # put application's code here

    if request.method == 'POST':
        query = request.form['query']
        tweets = api.search(q=query)
        print("test string", TextBlob("life is pain and shit").sentiment)
        for tweets in tweets:
            print(TextBlob("life is wonderful, and shit").sentiment)
            break

        return render_template('results.html', query = tweets)

    return render_template('404.html')




if __name__ == '__main__':
    app.run()
