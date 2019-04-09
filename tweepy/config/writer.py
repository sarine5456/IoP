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

import csv


def write_tweet(file_path, tweet):
    with open(file_path, 'a') as csv_file:
        writer = csv.DictWriter(csv_file, tweet.keys())
        writer.writerow(tweet)
        csv_file.close()


