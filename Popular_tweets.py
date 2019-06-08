#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


filename = "./Project_dataset/Wildfire/campfire--2018-11-01--2019-03-01.csv"


# In[3]:


# top retweets
def top_retweets(filename):
    '''
    Get top 0.05 percent or 10 tweets with most retweets from an event
    Input:
        filename: string
    Output:
        dataframe showing the tweets
    '''
    assert isinstance(filename,str)
    
    tweets_df = pd.read_csv(filename)
    n = tweets_df.shape[0]  # data numbers
    top_n = max(int(n*0.0005), 10)  # top 0.05 percent or 10 tweets
    topretweets_df = tweets_df.nlargest(top_n, 'retweets')
    pd.options.display.max_colwidth = 10000
    return topretweets_df[['username','retweets','favorites','text']]


# In[4]:


top_retweets(filename)


# In[5]:


# top favorites
def top_favorites(filename):
    '''
    Get top 0.05 percent or 10 tweets with most favorites from an event
    Input:
        filename: string
    Output:
        dataframe showing the tweets
    '''
    assert isinstance(filename,str)
    
    tweets_df = pd.read_csv(filename)
    n = tweets_df.shape[0]  # data numbers
    top_n = max(int(n*0.0005), 10)  # top 0.05 percent or 10 tweets
    topfav_df = tweets_df.nlargest(top_n, 'favorites')
    pd.options.display.max_colwidth = 10000
    return topfav_df[['username','retweets','favorites','text']]


# In[6]:


top_favorites(filename)


# In[7]:


# top retweets + favorites
def top_ret_fav(filename):
    '''
    Get top 0.05 percent or 10 tweets with most retweets plus favorites from an event
    Input:
        filename: string
    Output:
        dataframe showing the tweets
    '''
    assert isinstance(filename,str)
    
    tweets_df = pd.read_csv(filename)
    n = tweets_df.shape[0]  # data numbers
    top_n = max(int(n*0.0005), 10)  # top 0.05 percent or 10 tweets
    tweets_df['sums'] = tweets_df['retweets'] + tweets_df['favorites']
    topsums_df = tweets_df.nlargest(top_n, 'sums')
    pd.options.display.max_colwidth = 10000
    return topsums_df[['username','sums','retweets','favorites','text']]


# In[8]:


top_ret_fav(filename)


# In[9]:


# top retweets to favorites ratio 
def top_ret_to_fav_ratio(filename):
    '''
    Get top 0.05 percent or 10 tweets with most retweets plus favorites from an event
    Input:
        filename: string
    Output:
        dataframe showing the tweets
    '''
    assert isinstance(filename,str)
    
    tweets_df = pd.read_csv(filename)
    n = tweets_df.shape[0]  # data numbers
    top_n = max(int(n*0.0005), 10)  # top 0.05 percent or 10 tweets
    filtTweets_df = tweets_df[tweets_df.retweets > 1000] # only analyze popular tweets 
    
    assert(all(filtTweets_df['favorites'] > 0))
    ratio = filtTweets_df.retweets/filtTweets_df.favorites
    filtTweets_df.loc[:,'ratio'] = ratio
    topratios_df = filtTweets_df.nlargest(top_n, 'ratio')
    pd.options.display.max_colwidth = 10000
    
    return topratios_df[['username','ratio','retweets','favorites','text']]


# In[10]:


top_ret_to_fav_ratio(filename)


# In[ ]:





# In[ ]:




