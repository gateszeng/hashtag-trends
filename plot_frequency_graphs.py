import numpy as np
import pandas as pd
from matplotlib import pyplot
import matplotlib as mpl
from analysis_frequency import *

# Visualization of hashtag datasets
def plotHashtags(event_name, hashtags, dates, target_hashtag, daterange=None):
    '''
    Plots the frequency graph of all of the hashtags, highlighting the target_hashtag
    Args:
        event_name: (str) name of major event
        hashtags: (list) the hashtag names listed on the dataset files
        dates: (list) the start/end dates listed on the dataset files
        target_hashtag: (str) the name of the hashtag that we want to highlight
        daterange: (list) a different start/end date to zoom in on the data
    Returns:
        Matplotlib plot of the frequency of all of the hashtags
    '''
    #%matplotlib inline
    mpl.rcParams['figure.dpi'] = 150
    pyplot.rcParams['figure.figsize'] = (10, 5)

    # if the daterange parameter was not specified
    if not daterange:
        daterange = dates
    freqs_dict = {}

    # generate list of filenames
    filenames = ['./'+event_name+'/'+x+'--'+dates[0]+'--'+dates[1]+'.csv' for x in hashtags]
    for tag, filename in zip(hashtags, filenames):
        freqs_dict[tag] = normalizeFrequency(getFrequency(filename)[1].loc[daterange[0]: daterange[1]])

    # plot timeseries data
    for tag, freq in freqs_dict.items():
        if tag == target_hashtag:
            freq.plot(label=tag)
        else:
            freq.plot(zorder=1, alpha=0.25, label=tag)

    pyplot.legend(loc='upper right')
    pyplot.ylabel('popularity')
    pyplot.xlabel('date')
    pyplot.show()

def plotSpecificEvent(event_name):
    '''
    Given the base name of one of our major events, plot frequency graphs associated with it
    Args:
        event_name: (str) the name of the major event
    Returns:
        matplotlib.pyplots of the frequency graphs
    '''
    # List of hashtags/dates associated with each major event
    hashtags_falconheavy = ['falconheavy', 'spacex', 'tesla', 'falcon9', 'elonmusk']
    hashtags_campfire = ['campfire', 'californiafires', 'campfirejameswoods', 'paradise', 'woolseyfire']
    hashtags_metoo = ['metoo', 'believesurvivors', 'resist', 'stopkavanaugh', 'kavanaugh', 'timesup', 'trump', 'maga']
    hashtags_parkland = ['parkland', 'neveragain', 'marchforourlives', 'gunreformnow', 'guncontrolnow']
    hashtags_royalwedding = ['royalwedding', 'royalwedding2018', 'harryandmeghan', 'meghanmarkle', 'princeharry']
    dates_falconheavy = ['2018-02-01','2019-07-01']
    dates_campfire = ['2018-11-01', '2019-03-01']
    dates_metoo = ['2017-09-30', '2018-10-15']
    dates_parkland = ['2018-01-29', '2018-08-14']
    dates_royalwedding = ['2017-11-09', '2018-08-19']

    # dictionary to map major event to hashtags/dates
    event_dict = {}
    event_dict['falconheavy'] = [hashtags_falconheavy, dates_falconheavy]
    event_dict['campfire'] = [hashtags_campfire, dates_campfire]
    event_dict['metoo'] = [hashtags_metoo, dates_metoo]
    event_dict['parkland'] = [hashtags_parkland, dates_parkland]
    event_dict['royalwedding'] = [hashtags_royalwedding, dates_royalwedding]

    # verify event_name is valid
    assert isinstance(event_name, str)
    assert event_name in event_dict.keys()

    # make the plots
    plot_hashtag, plot_dates = event_dict[event_name]
    for t in plot_hashtag:
        print(t, flush=True)
        plotHashtags(event_name, plot_hashtag, plot_dates, t)
