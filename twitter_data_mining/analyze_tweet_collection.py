'''
script for analyzing first tweet_collection.txt file
'''
import json

__author__ = 'girish'

if __name__ == "__main__":
    tweets_file = open('tweet_collection_01-11-2015-01:00:16.txt')
    tweets_data = []
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            if 'ford' in tweet['text']:
                print tweet['text']
            tweets_data.append(tweet)
        except:
            continue

    print len(tweets_data)