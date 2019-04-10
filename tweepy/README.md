# Listening to twitter

For listening to tweets we recommended the use of tweepy. [tweepy](https://github.com/tweepy/tweepy) is a user friendly python library for listening to tweets using the listen
Find in this folder a simple implementation of this library suitable to listen to tweets using the Twitter streaming API

## Requirements
To work with this implementation you have to be sure of having "tweepy" and your credentials from the [Twitter Developer App](https://developer.twitter.com/en/apps).
You can install tweepy using pip:

        pip install tweepy  
        
## Twitter objects
In order to properly setup the twitter map section of the script it is a good idea to check out the kind of objects that a tweet contains.
[Tweet objects](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json.html)