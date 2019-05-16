
# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito & Sarine Bekarian
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
2016_01_JAN_listings = pd.read_csv('../data/airbnb_listings_sarine/2016_01_JAN_listings.csv')
2016_11_NOV_listings = pd.read_csv('../data/airbnb_listings_sarine/2016_11_NOV_listings.csv')
2016_12_DEC_listings = pd.read_csv('../data/airbnb_listings_sarine/2016_12_DEC_listings.csv')
2017_01_JAN_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_01_JAN_listings.csv')
2017_02_FEB_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_02_FEB_listings.csv')
2017_03_MAR_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_03_MAR_listings.csv')
2017_04_APR_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_04_APR_listings.csv')
2017_05_MAY_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_05_MAY_listings.csv')
2017_06_JUN_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_06_JUN_listings.csv')
2017_07_JUL_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_07_JUL_listings.csv')
2017_08_AUG_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_08_AUG_listings.csv')
2017_09_SEP_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_09_SEP_listings.csv')
2017_10_OCT_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_10_OCT_listings.csv')
2017_11_NOV_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_11_NOV_listings.csv')
2017_12_DEC_listings = pd.read_csv('../data/airbnb_listings_sarine/2017_12_DEC_listings.csv')
2018_01_JAN_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_01_JAN_listings.csv')
2018_02_FEB_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_02_FEB_listings.csv')
2018_03_MAR_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_03_MAR_listings.csv')
2018_04_APR_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_04_APR_listings.csv')
2018_05_MAY_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_05_MAY_listings.csv')
2018_06_JUN_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_06_JUN_listings.csv')
2018_07_JUL_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_07_JUL_listings.csv')
2018_08_AUG_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_08_AUG_listings.csv')
2018_09_SEP_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_09_SEP_listings.csv')
2018_10_OCT_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_10_OCT_listings.csv')
2018_11_NOV_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_11_NOV_listings.csv')
2018_12_DEC_listings = pd.read_csv('../data/airbnb_listings_sarine/2018_12_DEC_listings.csv')
2019_01_JAN_listings = pd.read_csv('../data/airbnb_listings_sarine/2019_01_JAN_listings.csv')
2019_02_FEB_listings = pd.read_csv('../data/airbnb_listings_sarine/2019_02_FEB_listings.csv')
2019_03_MAR_listings = pd.read_csv('../data/airbnb_listings_sarine/2019_03_MAR_listings.csv')
2019_04_APR_listings = pd.read_csv('../data/airbnb_listings_sarine/2019_04_APR_listings.csv')


######################################################
# Merging files
2016_01_JAN_listings['month'] = '2016-01'
2016_11_NOV_listings['month'] = '2016-11'
2016_12_DEC_listings['month'] = '2016-12'
2017_01_JAN_listings['month'] = '2017-01'
2017_02_FEB_listings['month'] = '2017-02'
2017_03_MAR_listings['month'] = '2017-03'
2017_04_APR_listings['month'] = '2017-04'
2017_05_MAY_listings['month'] = '2017-05'
2017_06_JUN_listings['month'] = '2017-06'
2017_07_JUL_listings['month'] = '2017-07'
2017_08_AUG_listings['month'] = '2017-08'
2017_09_SEP_listings['month'] = '2017-09'
2017_10_OCT_listings['month'] = '2017-10'
2017_11_NOV_listings['month'] = '2017-11'
2017_12_DEC_listings['month'] = '2017-12'
2018_01_JAN_listings['month'] = '2018-01'
2018_02_FEB_listings['month'] = '2018-02'
2018_03_MAR_listings['month'] = '2018-03'
2018_04_APR_listings['month'] = '2018-04'
2018_05_MAY_listings['month'] = '2018-05'
2018_06_JUN_listings['month'] = '2018-06'
2018_07_JUL_listings['month'] = '2018-07'
2018_08_AUG_listings['month'] = '2018-08'
2018_09_SEP_listings['month'] = '2018-09'
2018_10_OCT_listings['month'] = '2018-10'
2018_11_NOV_listings['month'] = '2018-11'
2018_12_DEC_listings['month'] = '2018-12'
2019_01_JAN_listings['month'] = '2019-01'
2019_02_FEB_listings['month'] = '2019-02'
2019_03_MAR_listings['month'] = '2019-03'
2019_04_APR_listings['month'] = '2019-04'

listings = pd.concat([2016_01_JAN_listings, 2016_11_NOV_listings, 2016_12_DEC_listings, 2017_01_JAN_listings, 2017_02_FEB_listings,
                      2017_03_MAR_listings, 2017_04_APR_listings, 2017_05_MAY_listings, 2017_06_JUN_listings, 2017_07_JUL_listings,
                      2017_08_AUG_listings, 2017_09_SEP_listings, 2017_10_OCT_listings, 2017_11_NOV_listings, 2017_12_DEC_listings,
                      2018_01_JAN_listings, 2018_02_FEB_listings, 2018_03_MAR_listings, 2018_04_APR_listings, 2018_05_MAY_listings,
                      2018_06_JUN_listings, 2018_07_JUL_listings, 2018_08_AUG_listings, 2018_09_SEP_listings, 2018_10_OCT_listings,
                      2018_11_NOV_listings, 2018_12_DEC_listings, 2019_01_JAN_listings, 2019_02_FEB_listings, 2019_03_MAR_listings,
                      2019_04_APR_listings])

# Cleaining data from price
listings['price_num'] = pd.to_numeric(listings['price'].str.replace('$', '').str.replace(',', ''))


# Calculate the average price per neighbourhood
# nbh_group = listings.groupby(['month', 'neighbourhood'])
# price_mean = nbh_group['price_num'].mean()
# price_mean = price_mean.to_frame()
# price_mean.columns = ['price_mean']
# price_mean.plot()

# Calculate the sum of reviews per neighbourhood
nbh_group = listings.groupby(['month', 'neighbourhood'])
review_sum = nbh_group['number_of_reviews'].sum()
review_sum = review_sum.to_frame()
review_sum.columns = ['review_sum']
review_sum.plot()


# price_mean.to_csv('../data/price_mean.csv')
review_sum.to_csv('../data/review_sum.csv')
