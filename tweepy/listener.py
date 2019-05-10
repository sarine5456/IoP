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

import datetime
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

    # attempts counter and time span for controlling sleep time
    attempts = 0
    sleep_time = 600

    # Handling twitter http connection error
    while True:
        try:
            print('Starting listening streaming at %s' % str(datetime.datetime.now()))
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
        except:
            print('Error in connection. %i times at %s' % (attempts, str(datetime.datetime.now())))
            if attempts < 1:
                time.sleep(sleep_time)
            elif attempts < 3:
                time.sleep((attempts+1)*sleep_time)
            else:
                time.sleep(attempts*sleep_time)
                attempts = 0
            attempts = attempts + 1

<<<<<<< HEAD
    # if you want to listen to a set of keywords use this line, you can combine with the location option
    # stream.filter(track=['your_keyword', 'second_keyword'])
    # stream.filter(track=['your_keyword', 'second_keyword'], locations=[2.0434, 41.2510, 2.4227, 41.5030])

    # if you want to listen to a set of tweets posted within a certain bounding box use this line and if you
    # want to listen to multiple locations use an array with a sequence of coordinates (groups of 4)
    # stream.filter(locations=[2.0434, 41.2510, 2.4227, 41.5030])
    # stream.filter(locations=[2.0434, 41.2510, 2.4227, 41.5030, -75.6599, 6.1282, -75.5066, 6.3688])

    # test Barcelona and 5 other cities
    stream.filter(locations=[2.095721, 41.334026, 2.242, 41.459385, 13.082829, 52.335389, 13.763982, 52.677764, 24.3605, 59.2484, 25.1296, 59.5988, 24.865916, 60.127921, 25.096629, 60.219994, -71.406732, 46.730272, -71.146215, 46.916796, 139.58336, 35.535362, 139.919587, 35.818562])

    # Coordinates of 6 cities
    # 2.095721, 41.334026, 2.242, 41.459385                 Barcelona
    # 13.082829, 52.335389, 13.763982, 52.677764            Berlin
    # 24.3605, 59.2484, 25.1296, 59.5988                    Tallinn
    # 24.865916, 60.127921, 25.096629, 60.219994            Helsinki
    # -71.406732, 46.730272, -71.146215, 46.916796          Quebec
    # 139.58336, 35.535362, 139.919587, 35.818562           Tokyo

=======
>>>>>>> upstream/master

