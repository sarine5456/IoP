# license: Creative Commons License
# Title: IoP Seminar by www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script contains lines of code from tweepy https://github.com/tweepy/tweepy


from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from config import credentials
from config import writer
from config import tweetMap

import time
import random

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

# Now the file path where the tweet's data will b e stored
file_path = 'tweets/tweets.csv'
counter = 0

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        tweet_line = tweetMap.map_tweet(data)
#        print(tweet_line.values)
        writer.write_tweet(file_path, tweet_line)
        return True

    def on_error(self, status):
        # if there is an error,
        print(status)
        nsecs = random.randint(60, 63)
        time.sleep(nsecs)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    # stream.filter(locations=[2.0434, 41.2510, 2.4227, 41.5030])

    # if you want to listen to a set of keywords use this line, you can combine with the location option
    # stream.filter(track=['your_keyword', 'second_keyword'])
    # stream.filter(track=['your_keyword', 'second_keyword'], locations=[2.0434, 41.2510, 2.4227, 41.5030])

    # if you want to listen to a set of tweets posted within a certain bounding box use this line and if you
    # want to listen to multiple locations use an array with a sequence of coordinates (groups of 4)
    # stream.filter(locations=[2.0434, 41.2510, 2.4227, 41.5030])
    # stream.filter(locations=[2.0434, 41.2510, 2.4227, 41.5030, -75.6599, 6.1282, -75.5066, 6.3688])

    # test Barcelona and Paris
    stream.filter(locations=[1.581, 48.429, 3.053, 49.197, 2.0434, 41.2510, 2.4227, 41.5030])

    # Some testing coordinates
    # 2.0434, 41.2510, 2.4227, 41.5030      Barcelona
    # -75.6599, 6.1282, -75.5066, 6.3688    Medellin
    # 1.581, 48.429, 3.053, 49.197          Paris
