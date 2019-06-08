from collections import defaultdict
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import os
import string
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


def get_freq_words_hastag(n = 30, filename = "Twitter-Get-Old-Tweets-Scraper/wedding/tweets_gathered_wedding_#harryandmeghan.csv"):
    '''
    print out most frequent words given a hashtag
    Input:
        n: number of frequent words desired (i.e: 30)
        filename: csvfile of certain hashtag
        (i.e: "tweets_gathered_wedding_#harryandmeghan.csv")
        
    Return: 
        maxkey: most frequent words
        maxperctg: percentage of these words
    '''

    word_dict = defaultdict(int)
    stop_words = set(stopwords.words('english'))
    punctuations = string.punctuation
    tweet_ids = [] 
    lines = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        sublines=[]
        for i,row in enumerate(csv_reader):
            if i >0 and (row[9] not in tweet_ids):
                tweet_ids.append(row[9])
                sublines.append(row[5])
                lines.append(row[5])
        print("finished file {} >> {} lines ({})".format(filename,len(lines), len(sublines)))
    i=0
    for line in lines:
        subline=line.lower().split()
        for s in subline:
            if (s not in stop_words) and (s not in punctuations) and (not s.startswith('#')) and (not s.startswith(".")) :
                word_dict[s] += 1
        i+=1

    maxkey = sorted(word_dict, key=word_dict.get, reverse=True)[:n]

    maxvalues = [word_dict[s] for s in maxkey]
    result_dict={}
    for i in range(len(maxkey)):
        result_dict[maxkey[i]] =maxvalues[i]/len(lines)
    return result_dict

def get_corr_df(directory, hashtags, n=30):
    '''
    Analyze the relevance between tweets' texts from popular hashtags of each events
    Input:
        directory: filepath of csvfile of certain hashtag
        hashtags: a list of hashtags names
        n: number of frequent words desired (i.e: 30)
    Output:
        corr_df: a dataframe contains correlation values between hashtags
    '''
    assert isinstance(directory,list)
    assert isinstance(hashtags,list)
    assert isinstance(n,int) and n>0
    
    corr_list = []
    N = len(directory)
    corr_matr = np.zeros((N, N))
    n = 30
    dict_set = []
    for i in range(N):
        dict_set = dict_set + [get_freq_words_hastag(n, "./Project_dataset/"+directory[i])]
    
    for i in range(N):
        for j in range(N-i):
            dict_1 = dict_set[i]
            dict_2 = dict_set[j+i]
            temp = {x:dict_1[x]*dict_2[x] for x in dict_1 if x in dict_2}
            corr_list = corr_list + [[i, j+i, sum(temp.values())]]
            corr_matr[i, j+i] = sum(temp.values())
            corr_matr[j+i, i] = sum(temp.values())
    corr_matr = corr_matr/corr_matr.max()
    corr_df = pd.DataFrame(corr_matr,index = hashtags)
    corr_df.columns = hashtags
    return corr_df

def plot_corr(corr_df,title):
    '''
    Plot the relevance between tweets' texts from popular hashtags of each events
    Input:
        corr_df: a dataframe contains correlation values between hashtags
        title: event name, string
    Output:
        A heatmap presents the correlation between hashtags
    '''
    
    assert isinstance(corr_df,pd.DataFrame)
    assert isinstance(title,str)
    
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(20, 10, as_cmap=True)
    mask = np.zeros_like(corr_df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    sns.heatmap(corr_df, mask=mask, annot=True, cmap ='YlOrRd', vmax = 1,
                square=True, linewidths=.5, cbar_kws={"shrink": .7}, annot_kws={"size": 14})
    plt.yticks(rotation=0, fontsize=18) 
    plt.xticks(rotation=45, fontsize=18) 
    plt.title(title+" Hashtag Relevance", fontsize=18)

    return sns.heatmap

def datacounts(directory, hashtags):
    '''
    Count and sort the hashtag usage of each events
    Input:
        directory: filepath of csvfile of certain hashtag
        hashtags: a list of hashtags names
    Output:
        count_df: a dataframe contains sorted hashtag counts
    '''
    
    assert isinstance(directory,list)
    assert isinstance(hashtags,list)
    import csv
    N = len(directory)
    count = np.zeros(N)
    for i in range(N):
        tmp_count = 0
        filename = "./Project_dataset/"+directory[i]
        with open(filename) as f:
            cr = csv.reader(f)
            for row in cr:
                tmp_count += 1
        count[i] = tmp_count
    count_df = pd.DataFrame({'counts' : count},index = hashtags)
    count_df = count_df.sort_values(by=['counts'])

    return count_df

directory = ["RoyalWedding/harryandmeghan--2017-11-09--2018-08-19.csv",
             "RoyalWedding/meghanmarkle--2017-11-09--2018-08-19.csv",
             "RoyalWedding/princeharry--2017-11-09--2018--08-19.csv",
             "RoyalWedding/royalwedding2018--2017-11-09--2018--08-19.csv",
             "RoyalWedding/royalweding--2017-11-09--2018--08-19.csv"]
hashtags = ["harryandmeghan", "meghanmarkle", "princeharry", "royalwedding2018", "royalwedding"]
corr_df = get_corr_df(directory, hashtags, n=50)
plot_corr(corr_df,"Royal Wedding")

directory = ["Shooting/guncontrolnow--2018-01-29--2018-08-14.csv",
             "Shooting/gunreformnow--2018-01-29--2018-08-14.csv",
             "Shooting/marchforourlives--2018-01-29--2018-08-14.csv",
             "Shooting/neveragain--2018-01-29--2018-08-14.csv",
             "Shooting/parkland--2018-01-29--2018-08-14.csv"]
hashtags = ["guncontrolnow", "gunreformnow", "marchforourlives", "neveragain", "parkland"]
corr_df = get_corr_df(directory, hashtags, n=30)
Gun_count = datacounts(directory, hashtags)
plot_corr(corr_df,"Parkland")

directory = ["SpaceX/elonmusk--2018-02-01--2019-07-01.csv",
             "SpaceX/falcon9--2018-02-01--2019-07-01.csv",
             "SpaceX/falconheavy--2018-02-01--2019-07-01.csv",
             "SpaceX/spacex--2018-02-01--2019-07-01.csv",
             "SpaceX/tesla--2018-02-01--2019-07-01.csv"]
hashtags = ["elonmusk", "falcon9", "falconheavy", "spacex", "tesla"]
corr_df = get_corr_df(directory, hashtags, n=50)
SX_count = datacounts(directory, hashtags)
plot_corr(corr_df,"SpaceX")

directory = ["SpaceX/elonmusk--2018-02-01--2019-07-01.csv",
             "SpaceX/falcon9--2018-02-01--2019-07-01.csv",
             "SpaceX/falconheavy--2018-02-01--2019-07-01.csv",
             "SpaceX/spacex--2018-02-01--2019-07-01.csv",
             "SpaceX/tesla--2018-02-01--2019-07-01.csv"]
hashtags = ["elonmusk", "falcon9", "falconheavy", "spacex", "tesla"]
corr_df = get_corr_df(directory, hashtags, n=50)
SX_count = datacounts(directory, hashtags)
plot_corr(corr_df,"SpaceX")

directory = ["Wildfire/californiafires--2018-11-01--2019-03-01.csv",
             "Wildfire/campfire--2018-11-01--2019-03-01.csv",
             "Wildfire/campfirejameswoods--2018-11-01--2019-03-01.csv",
             "Wildfire/paradise--2018-11-01--2019-03-01.csv",
             "Wildfire/woolseyfire--2018-11-01--2019-03-01.csv"]
hashtags = ["californiafires", "campfire", "campfirejameswoods", "paradise", "woolseyfire"]
corr_df = get_corr_df(directory, hashtags, n=30)
WF_count = datacounts(directory, hashtags)
plot_corr(corr_df,"Wildfire")

directory = ["MeToo/believesurvivors--2017-09-30--2018-10-15.csv",
             "MeToo/kavanaugh--2017-09-30--2018-10-15.csv",
             "MeToo/maga--2017-09-30--2018-04-09.csv",
             "MeToo/MeToo--2017-09-30--2018-10-15.csv",
            "MeToo/resist--2017-09-30--2018-10-15.csv",
            "MeToo/stopkavanaugh--2017-09-30--2018-10-15.csv",
            "MeToo/timesup--2017-09-30--2018-10-15.csv",
            "MeToo/trump--2017-09-30--2018-04-11.csv"]
hashtags = ["believesurvivors", "kavanaugh", "maga", "MeToo", "resist", "stopkavanaugh",
           "timesup", "trump"]
corr_df = get_corr_df(directory, hashtags, n=30)
MeToo_count = datacounts(directory, hashtags)
plot_corr(corr_df,"MeToo")
