# license: Creative Commons License
# Title: IoP Seminar by www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script contains lines of code from tweepy https://github.com/tweepy/tweepy
#
# Description: This script sets up the file whe from your developer's twitter account
# and servers for being stored apart from the main script.

import json
from geojson import Point
from geojson import Feature


def map_tweet(tweet):
    tweet_dict = json.loads(tweet)

    user = tweet_dict['user']
    entities = tweet_dict['entities']
    properties = dict()
    properties['id'] = tweet_dict['id_str']
    properties['text'] = tweet_dict['text'].replace('\n', '|| ').encode("utf-8")
    properties['user'] = user['screen_name']
    properties['user_followers'] = user['followers_count']
    properties['created_at'] = tweet_dict['created_at']
    properties['timestamp_ms'] = tweet_dict['timestamp_ms']
    properties['quote_count'] = tweet_dict['quote_count']
    properties['reply_count'] = tweet_dict['reply_count']
    properties['retweet_count'] = tweet_dict['retweet_count']
    properties['favorite_count'] = tweet_dict['favorite_count']
    properties['url'] = entities['urls'] #when there are more than one

    # Check if tweet is geo and fill a new set of properties
    is_geo = tweet_dict['geo']
    if is_geo:
        print('is_geo')
        print(tweet_dict['coordinates'])
        coord_list = tweet_dict['coordinates']
        properties['lat'] = coord_list['coordinates'][0]
        properties['lon'] = coord_list['coordinates'][1]

        # Check if geo-location is related to a place
        place = tweet_dict['place']
        if place:
            try:
                properties['place_type'] = place['place_type']
                properties['place_name'] = place['name']
                properties['place_full_name'] = place['full_name']
                bbox = place['bounding_box']
                properties['place_min_lat'] = bbox['coordinates'][0][0][0]
                properties['place_min_lon'] = bbox['coordinates'][0][0][1]
                properties['place_max_lat'] = bbox['coordinates'][0][3][0]
                properties['place_max_lon'] = bbox['coordinates'][0][3][1]
            except:
                properties['place_type'] = properties['place_name'] = properties['place_full_name'] = ''
                properties['place_min_lat'] = properties['place_min_lon'] = properties['place_max_lat'] = \
                    properties['place_max_lon'] = ''

    else:
        properties['lat'] = properties['lon'] = ''
        properties['place_type'] = properties['place_name'] = properties['place_full_name'] = ''
        properties['place_min_lat'] = properties['place_min_lon'] = ''

    return properties


def return_line():
    return 'line \n'



    # location, text, timeline, language, "quote_count": 1455,
    # 		"reply_count": 404,
    # 		"retweet_count": 13145,
    # 		"favorite_count": 104609,
    # hashtags, urls (other social networks)
    # timestamp_ms