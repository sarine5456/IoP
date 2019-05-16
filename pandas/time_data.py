
# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# This script uses geopandas for data management for more information visit; geopandas.org/

import pandas as pd
import matplotlib.pyplot as plt
from pandas import plotting


plotting.register_matplotlib_converters()


######################################################
# Read a csv file
tweets = pd.read_csv('../data/tweets_b.csv')

# Time data formats are diverse. one of those formats (and the most reliable) is milliseconds after the epoch

# Raw data in miliseconds
print('This is an example of time in milliseconds')
print(tweets['timestamp_ms'][10])

# Using pandas function to transform ms into readable datetime values (be careful with the units
print('Now the same example in a human-readable datetime format')
print(pd.to_datetime(tweets['timestamp_ms'][10], unit='ms'))

# adding a new column for datetime values
tweets['time'] = pd.to_datetime(tweets['timestamp_ms'], unit='ms')



######################################################
# Plots using time
fig, ax = plt.subplots()
ax.scatter(tweets['time'], tweets['user_screen_name'], alpha=0.3, s=2)
plt.title('Scatter plot using tweets')
plt.show()


# Changing y-axis value order and adding colors
tweets.sort_values('user_screen_name', ascending=False, inplace=True)
fig, ax = plt.subplots()
ax.scatter(tweets['time'], tweets['user_screen_name'], s=2)
plt.title('Scatter ordered by user posting tweets')
plt.show()


