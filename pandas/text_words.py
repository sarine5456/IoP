
# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/

import re
import pandas as pd
import matplotlib.pyplot as plt
from pandas import plotting
import itertools


plotting.register_matplotlib_converters()


######################################################
# Read a csv file
tweets = pd.read_csv('../data/tweets_s.csv')

# adding a new column for datetime values
tweets['time'] = pd.to_datetime(tweets['timestamp_ms'], unit='ms')


# Counting individual words from the text
text_example = tweets['text'][20]
print('A tweet text with the number of words:')
print(text_example)
words_example = re.split(r"\s", text_example)
print('Words: %i' % len(words_example))


# Counting words from the entire set of tweets
words = tweets['text'].str.split(r"\s")
words = pd.DataFrame(itertools.chain(*words))
print('Total words: %i' % len(words))

# Plotting top words
words['words'] = words                          # This line does not make any sense but it is needed for plotting
count_words = words['words'].value_counts()

# top users
top_words = count_words.nlargest(100)
fig, ax = plt.subplots()
top_words.plot(kind='barh', title="Top users")
plt.show()



