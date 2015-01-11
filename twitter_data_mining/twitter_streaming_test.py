'''
Testing twitter streaming using twitter library
'''
import json

from twitter.oauth import OAuth
from twitter.stream import TwitterStream
from tweepy import StreamListener, OAuthHandler, Stream


__author__ = 'girish'


def streamUsingTwitterMaster(auth):
    global twitter_stream, iterator, collectionFile, tweet
    twitter_stream = TwitterStream(auth=auth,
                                   domain='stream.twitter.com/1.1/statuses/filter.json?track=leagueoflegends')
    iterator = twitter_stream.statuses.sample()
    for tweet in iterator:
        print tweet


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == "__main__":
    consumer_key = "wdJV2pAOnksaRAbB1HUcS6H7P"
    consumer_secret = "BsGUbPSpiYa9BNwcai6xa2eLSzI25jDOUDSR9ZTm8AaWpGsa9Z"
    access_token = "2245889773-K4eVW0aIMxEdmg1JMjfxvV3eKMUkR2IUvCAOgyq"
    access_secret = "M0S3hwHpIzMWhUUQItvSGpYhwcDqGWSpfrM9uDuEv7brV"
    auth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

    # streamUsingTwitterMaster(auth)

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['leagueoflegends', 'ford'])
