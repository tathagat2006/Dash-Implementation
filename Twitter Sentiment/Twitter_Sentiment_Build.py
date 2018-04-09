from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time


consumer_key = 'IhmYtYbSp7yrADITwhJaY2lhQ'
consumer_secret = 'mmkrdMXv0ADfw2Zj4qIA7RkDcreX14IYgbDt26LhdVDylRy1jr'
access_token = '778635668339634176-DTq7Twl56ymsnyhrbAEX1Zk6NWPoicB'
access_token_secret = '03iN7IAxODFcmrCCey01YRsJ6BRHfI3LIvLWJBVe38swh'

analyzer = SentimentIntensityAnalyzer()

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()

class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)



while True:

    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["a","e","i","o","u"])
    except Exception as e:
        print(str(e))
        time.sleep(5)

# auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
# auth.set_access_token(access_token , access_token_secret)
# api=tweepy.API(auth , wait_on_rate_limit = True)