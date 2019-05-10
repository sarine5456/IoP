# Listening to twitter

For listening to tweets we recommended the use of tweepy. [tweepy](https://github.com/tweepy/tweepy) is a user friendly python library for listening to tweets using the listen
Find in this folder a simple implementation of this library suitable to listen to tweets using the Twitter streaming API

## Requirements
To work with this implementation you have to be sure of having "tweepy" and your credentials from the [Twitter Developer App](https://developer.twitter.com/en/apps).
You can install tweepy using pip:

        pip install tweepy  
        pip install geojson
        
## Twitter objects
In order to properly setup the twitter map section of the script it is a good idea to check out the kind of objects that a tweet contains.
[Tweet objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html)

There are relevant elements in tweeter to consider during the analysis and the best source for understanding is the developers website. These are the main components of a tweet:
* [Tweet](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object): It contains most of the well known features of a tweet such as the text, timestamp, language, reply and retweets.
* [User](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object): it contains details from the account which posted the tweet.
* [Entities](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object): these are the additional features of a tweet such as hashtags, urls, mentions and symbols. They are usually arrays and need an special treatment.
* [Geo](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects): This is the main source of geospatial data, it is composed by two elements a point geometry made out of the coordinates which define tweet location and place which is an object describing a location (area) linked to a real entity.