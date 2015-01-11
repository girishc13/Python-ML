#!/bin/bash
DATE=$(date +"%m-%d-%Y-%T")
FILENAME="tweet_collection_$DATE.txt"
echo "Running tweet collection at $DATE......" 
python twitter_streaming_test.py > $FILENAME
