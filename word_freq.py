from collections import defaultdict
from nltk.corpus import stopwords
import os
import string
import numpy as np
from collections import defaultdict

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import requests
import matplotlib.pyplot as plt
import csv
import re




def get_freq_words_topic(n = 30,directory = "Twitter-Get-Old-Tweets-Scraper/gunshoot"):
    '''
    print out most frequent words given a topic
    Input:
        n: number of frequent words desired (i.e: 30)
        directory: the directory containing all excel file of certain topic 
        (i.e: "Twitter-Get-Old-Tweets-Scraper/gunshoot")
    Return: 
        maxkey: most frequent words
        maxperctg: percentage of these words
    
    '''
    assert isinstance(n, int)
    assert n > 0
    assert isinstance(directory, str)

    file_names = os.listdir(directory)
    assert file_names , "there must be files in this directory"
    if 'mergedfile.csv' in file_names:
        file_names.remove('mergedfile.csv')
    if '.DS_Store' in file_names:  
        file_names.remove('.DS_Store')
    #filename = "Twitter-Get-Old-Tweets-Scraper/tweets_gathered_wedding_#harryandmeghan.csv"
    word_dict = defaultdict(int)
    stop_words = set(stopwords.words('english'))
    punctuations = string.punctuation
    #f = open('filename')
    tweet_ids = [] 
    lines = []
    import csv
    for filename in file_names:
        dirname = directory +'/'+filename
        with open(dirname) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            sublines=[]
            for i,row in enumerate(csv_reader):
                if i >0 and (row[9] not in tweet_ids):
                    tweet_ids.append(row[9])
                    sublines.append(row[5])
                    lines.append(row[5])
            print("finished file {} >> {} lines ({})".format(filename,len(lines), len(sublines)))
    mergedName = directory+'/mergedfile.csv'
    
    with open(mergedName, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(["ID","content"])
        for i in range(len(lines)):
            writer.writerows([tweet_ids[i], lines[i]])
    writeFile.close()
    
    i=0
    for line in lines:
        subline=line.lower().split()
        for s in subline:
            if (s not in stop_words) and (s not in punctuations) and (not s.startswith('#')) and (not s.startswith(".")) :
                word_dict[s] += 1
        i+=1

    #sorted(word_dict.items(), key=lambda word_dict : word_dict[1])
    #print(word_dict)

    maxkey = sorted(word_dict, key=word_dict.get, reverse=True)[:n]

    maxvalues = [word_dict[s] for s in maxkey]
    result_dict={}
    for i in range(len(maxkey)):
        #print("{:20}   {:10}    {:.2f}%".format(maxkey[i], maxvalues[i], 100*maxvalues[i]/len(lines)))
        result_dict[maxkey[i]] =maxvalues[i]/len(lines)
    #maxperctg = 100*np.array(maxvalues)/len(lines)
    return result_dict



def get_freq_words_hastag(n = 30, filename = "Twitter-Get-Old-Tweets-Scraper/wedding/tweets_gathered_wedding_#harryandmeghan.csv"):
    '''
    print out most frequent words given a hashtag
    Input:
        n: number of frequent words desired (i.e: 30)
        filename: csvfile of certain hashtag
        (i.e: "tweets_gathered_wedding_#harryandmeghan.csv")
        
    Return: 
        result_dict: a dict whose keys are most frequ
        maxkey: most frequent words
        maxperctg: percentage of these words
    '''
    assert isinstance(n, int)
    assert n > 0
    assert isinstance(filename, str)
    #filename = "Twitter-Get-Old-Tweets-Scraper/tweets_gathered_wedding_#harryandmeghan.csv"
    word_dict = defaultdict(int)
    stop_words = set(stopwords.words('english'))
    punctuations = string.punctuation
    #f = open('filename')
    tweet_ids = [] 
    lines = []
    import csv
    
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
    result_dict=defaultdict(int)
    for i in range(len(maxkey)):
        result_dict[maxkey[i]] =maxvalues[i]/len(lines)
    #maxperctg = 100*np.array(maxvalues)/len(lines)
    return result_dict


def draw_bars(directory, topic ,freq_words):
    '''
    Input: 
        directory: Twitter-Get-Old-Tweets-Scraper/Spacex"
        topic: str (eq: "SpaceX")
        freq_words: freq_words_spacex = list(word_dict_spacex.keys())[1:]
        
    Output:
        Word Count Analysis bar chart : whose x-axis are most frequent wods 
        and y-axis is percentage
        
    Usage:
        directory_spacex=  "Twitter-Get-Old-Tweets-Scraper/Spacex"
        word_dict_spacex = get_freq_words_topic(n=11, directory = directory_spacex)
        freq_words_spacex = list(word_dict_spacex.keys())[1:]
        draw_bars(directory_spacex, "SpaceX", freq_words_spacex)

    '''
    assert isinstance(directory, str)
    assert isinstance(topic, str)
    assert isinstance(freq_words, list)


    import numpy as np
    import matplotlib.pyplot as plt
    from collections import defaultdict
    import re
    
    file_names = os.listdir(directory)
    if 'mergedfile.csv' in file_names:
        file_names.remove('mergedfile.csv')
    if '.DS_Store' in file_names:  
        file_names.remove('.DS_Store')

    word_dict_list = list()
    for i in range(5):
        word_dict_list.append(dict())

    hashtags = []

    for i, filename in enumerate(file_names):
        hashtags.append(re.findall("^(\w+)--",filename)[0])
        filename = directory + '/' + filename
        word_dict_list[i] = get_freq_words_hastag(n=500, filename = filename)

    data_list=[]
    for i in range(5):
        data_list.append(list())
    for w in freq_words:
        for i in range(5):
            data_list[i].append(word_dict_list[i][w])

    n_groups = len(freq_words)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8
    color = ['b','g','r','c','m']
    rect= [None]*5
    for i in range(5):
        rect[i] = plt.bar(index+bar_width*i, data_list[i] , bar_width,alpha=opacity,color=color[i],label=hashtags[i])

    plt.xlabel('Most Frequent Words')
    plt.ylabel('Percentage (%)')
    title = 'Wordcount Analysis of #Falconheavy'.format(topic)
    plt.title(title)
    plt.xticks(index + bar_width, freq_words, rotation = -40)

    plt.legend()
    plt.tight_layout()
    savefile_name = "word_count_analysis_{}".format(topic)
    plt.savefig(savefile_name,dpi=400)
    plt.show()


def generate_wordcloud(hashtag, words, mask):
    '''
    display and save word cloud
    Input
        hashtag: desired wordcloud name 
        words: list of words contained in the tweets
        mask: cloud shape image in png fornat 
        (eq: mask = np.array(Image.open("cloud.png")) 
    '''

    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    word_cloud.to_file("wordClouds/"+hashtag+".png")

def save_wordcloud(filename,mask):
    '''
    creat a wordcloud given hashtag excel file
    Input:
        filename: 
        mask: cloud shape image in png fornat 
        (eq: mask = np.array(Image.open("cloud.png")) 

    Output: 
        Save a wordcloud to png image

    '''
    assert isinstance(filename, str)
    #assert isinstance(mask, np.array)


    hashtag = re.findall('/(\w+)--',filename)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lines=[]
        tweet_ids = []
        text=""
        for i,row in enumerate(csv_reader):
            if i >0 and (row[9] not in tweet_ids):
                tweet_ids.append(row[9])
                lines.append(row[5].lower())
    csv_file.close()
    text = " ".join(lines)
    hashtags = re.findall(' (#\w+) ',text)
    pic_link = re.findall('(pic.twitter.com/\w+)',text)
    for h in hashtags:
        text= text.replace(h,"")
    for p in pic_link:
        text = text.replace(p,"")
    text = text.replace("https","")
    text = text.replace("twitter","")
        
    generate_wordcloud(hashtag[0], text, mask)