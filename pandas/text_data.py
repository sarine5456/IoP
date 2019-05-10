# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# This script uses geopandas for data management for more information visit; geopandas.org/

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######################################################
# Read a csv file
tweets = pd.read_csv('../data/tweets_s.csv')

# Text columns can have internal objects and regular expressions are very useful for dealing with this structures
# More info about regular expressions is available
# here https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html


#########################################################
# Text with HTML code format
print('This is an example with HTML Tag')
print(tweets['source'][20])
text = tweets['source'][20]
text = re.findall(r">(\D+)<", text)
print('This regular expression ">(\D+)" captures everything within > and <. result: %s' % text[0])

# To apply a regular expression to a data frame column we need to use str.extract
tweets['source_text'] = tweets['source'].str.extract(r">(\D+)<")
# there are some exceptions where 'nan' values can show up we use the numpy na value
tweets['source_text'] = tweets['source_text'].replace(np.nan, 'Unknown source')

# Adding a new column for datetime values
tweets['time'] = pd.to_datetime(tweets['timestamp_ms'], unit='ms')

# Now we can aggregate the data frame and see how many tweets were post by source
# Scatter plot showing tweets along a timeline
fig, ax = plt.subplots()
ax.scatter(tweets['time'], tweets['source_text'], alpha=0.3, s=2)
plt.show()


# Bar chart with the number of tweets per client (barh: for horizontal bar chart)
fig, ax = plt.subplots()
tweets_sources = tweets[["source_text"]].drop_duplicates()
ax = tweets['source_text'].value_counts().plot(kind='barh',
                                               title="Tweets per client")
plt.show()




#########################################################
# Text and json-like structure
print('This is an example of a JSON object inside a column')
print(tweets['hashtags'][24])

hashtags = tweets['hashtags'][24]
hashtags = re.findall(r": \W(\D+)\W,", tweets['hashtags'][24])


print('Using the regular expression ": \W(\D+)\W," we get the hashtags in a list format')
print(hashtags)

hashtags_list = tweets['hashtags'].str.extract(r": \W(\D+)\W,")
hashtags_list.columns = ['ht']
# We need to remove the nan values
hashtags_list = hashtags_list.dropna()
ht_count = hashtags_list['ht'].value_counts()
# getting only the top X values
ht_top = ht_count.nlargest(30)

# Bar chart with the count of hashtags (barh: for horizontal bar chart)
# try this out using a very a big file ;)
# fig, ax = plt.subplots()
# ax = ht_count.plot(kind='barh', title="HT count")
# plt.show()

# Bar chart with the top X hashtags (barh: for horizontal bar chart)
fig, ax = plt.subplots()
ax = ht_top.plot(kind='barh', title="Top HT")
plt.show()



#########################################################
# Save any dataframe to CSV File

ht_count.to_csv('../data/output.csv')

