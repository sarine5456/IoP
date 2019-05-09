
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
tweets = pd.read_csv('../data/tweets_s.csv')


# Counting tweets per user and showing the count in a bar chart
tweets_per_user = tweets['user_screen_name'].value_counts()
# fig, ax = plt.subplots()
# tweets_per_user.plot(kind='barh', title="Tweets per user")
# plt.show()

# top users
top_users = tweets_per_user.nlargest(200)
fig, ax = plt.subplots()
top_users.plot(kind='barh', title="Top users")
plt.show()

print('end of graphs')