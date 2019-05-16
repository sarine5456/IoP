
# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# Merging and joining data frames is a very important task in data science check out the docs
# Join: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html
# Merge: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
#

import pandas as pd
import matplotlib.pyplot as plt
from pandas import plotting


plotting.register_matplotlib_converters()


######################################################
# Read a csv file
listings_012018 = pd.read_csv('../data/airbnb_listings/listings_012018.csv')
listings_022018 = pd.read_csv('../data/airbnb_listings/listings_022018.csv')
listings_042018 = pd.read_csv('../data/airbnb_listings/listings_042018.csv')
listings_052018 = pd.read_csv('../data/airbnb_listings/listings_052018.csv')
listings_062018 = pd.read_csv('../data/airbnb_listings/listings_062018.csv')
listings_072018 = pd.read_csv('../data/airbnb_listings/listings_072018.csv')
listings_082018 = pd.read_csv('../data/airbnb_listings/listings_082018.csv')
listings_092018 = pd.read_csv('../data/airbnb_listings/listings_092018.csv')
listings_102018 = pd.read_csv('../data/airbnb_listings/listings_102018.csv')
listings_112018 = pd.read_csv('../data/airbnb_listings/listings_112018.csv')
listings_122018 = pd.read_csv('../data/airbnb_listings/listings_122018.csv')
listings_012019 = pd.read_csv('../data/airbnb_listings/listings_012019.csv')
listings_022019 = pd.read_csv('../data/airbnb_listings/listings_022019.csv')
listings_032019 = pd.read_csv('../data/airbnb_listings/listings_032019.csv')
listings_042019 = pd.read_csv('../data/airbnb_listings/listings_042019.csv')


######################################################
# Merging files
listings_012018['month'] = '2018-01'
listings_022018['month'] = '2018-02'
listings_042018['month'] = '2018-04'
listings_052018['month'] = '2018-05'
listings_062018['month'] = '2018-06'
listings_072018['month'] = '2018-07'
listings_082018['month'] = '2018-08'
listings_092018['month'] = '2018-09'
listings_102018['month'] = '2018-10'
listings_112018['month'] = '2018-11'
listings_122018['month'] = '2018-12'
listings_012019['month'] = '2019-01'
listings_022019['month'] = '2019-02'
listings_032019['month'] = '2019-03'
listings_042019['month'] = '2019-04'

listings = pd.concat([listings_012018, listings_022018, listings_042018, listings_052018, listings_062018,
                      listings_072018, listings_082018, listings_092018, listings_102018, listings_112018,
                      listings_122018, listings_012019, listings_022019, listings_032019, listings_042019])

# Count the number of listings per host and merge this count back
host_group = listings.groupby(['month', 'host_id'])
host_count = host_group['month'].count()
host_count = host_count.to_frame()
host_count.columns = ['count']
host_count['category'] = 'Sharing 1'
host_count.loc[host_count['count'] == 2, 'category'] = 'Sharing 2'
host_count.loc[host_count['count'] == 3, 'category'] = 'Sharing 3'
host_count.loc[host_count['count'] == 4, 'category'] = 'Sharing 4'
host_count.loc[host_count['count'] == 5, 'category'] = 'Sharing 5'
host_count.loc[host_count['count'] > 5, 'category'] = 'Business'
listings = listings.set_index(['month', 'host_id']).join(host_count)

listings_sharing_1 = listings[listings['category'] == 'Sharing 1'].groupby(['month'])
count_sharing_1 = listings_sharing_1['id'].count()
listings_sharing_2 = listings[listings['category'] == 'Sharing 2'].groupby(['month'])
count_sharing_2 = listings_sharing_2['id'].count()
listings_sharing_3 = listings[listings['category'] == 'Sharing 3'].groupby(['month'])
count_sharing_3 = listings_sharing_3['id'].count()
listings_sharing_4 = listings[listings['category'] == 'Sharing 4'].groupby(['month'])
count_sharing_4 = listings_sharing_4['id'].count()
listings_sharing_5 = listings[listings['category'] == 'Sharing 5'].groupby(['month'])
count_sharing_5 = listings_sharing_5['id'].count()
listings_business = listings[listings['category'] == 'Business'].groupby(['month'])
count_business = listings_business['id'].count()

count_sharing_1.plot(label='1 Listing')
count_sharing_2.plot(label='2 Listings')
count_sharing_3.plot(label='3 Listings')
count_sharing_4.plot(label='4 Listings')
count_sharing_5.plot(label='5 Listings')
count_business.plot(label='5+ Listings')
plt.ylim((0, 8500))
plt.legend()

listings.to_csv('../data/listings_categories.csv')
