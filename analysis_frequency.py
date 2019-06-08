import numpy as np
import pandas as pd
from matplotlib import pyplot
import matplotlib as mpl

def getFrequency(tag, dataset_name):
    '''
    Reads in data from a filepath
    Args:
        dataset_name: (str) filepath of dataset
    Returns:
        dataset_df, DataFrame containing all tweets, indexed by date
        counts, Series containing counts of tweets, indexed by date
    '''
    filepath = "./datasets/" + dataset_name

    dataset_df = pd.read_csv(filepath)
    params = dataset_name[:-4].split('--')
    date_df = pd.Series(0, index=pd.date_range(params[1], params[2]))

    filtered_dates = dataset_df.loc[:, ['date']]
    filtered_dates = filtered_dates.apply(lambda x: pd.to_datetime(x).dt.normalize())
    counts = filtered_dates.groupby('date').size()

    # merge dates and counts, so that we have all dates
    counts = (counts + date_df).fillna(0)

    return dataset_df, counts

def normalizeFrequency(freqs):
    '''
    Normalize the values in freqs
    Args:
        freqs: (Series) time-series count of tweets to normalize
    Returns:
        normalized Series of the frequency of tweets per day
    '''
    # min-max feature scaling to get values between 0 and 1
    freqs_norm = (freqs - freqs.min()) / (freqs.max() - freqs.min())
    return freqs_norm

def getTopPostFromDate(dataset_df, date):
    '''
    Lists the top tweets from a particular day in descending order
    Args:
        dataset_df: (DataFrame) the DataFrame for the tweets dataset
        date: (str) date that we want to look at
    Returns:
        a DataFrame showing the top tweets in descending order from the given day
    '''

    # grab tweets from most active day
    data_df.loc[:, 'date'] = data_df.loc[:, 'date'].apply(lambda x: pd.to_datetime(x).normalize())
    top_df = data_df.groupby(by='date').get_group(date)
    top_df = top_df.sort_values('favorites', ascending=False)

    return top_df
