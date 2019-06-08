# Hashtags of Major Events (Group 17)

## Team Members
 - Gates Zeng (@gateszeng)
 - Wei-Cheng Huang (@tommyhuangtw)
 - Yayu Lin ()

## Problem
Analysing the trends of popular hashtags surrounding major world events

## Summary
 * Using hashtags could gain more popularity 
 * Using more specific hashtag could gain more popularity toward specific topic
 * Nearly all popular posts tend to use pictures
 * Top tweets in social movement categories have more text than in entertainment

## Methodology
 #### Data Collection and Cleanup
  * Twitter-Get-Old-Tweets-Scraper (with modifications)
  * Chose a major event
    * Scraped a “seed” hashtag representing the event
    * Then scraped tweets from top hashtags in original set
  * Chose time period
    * Starting before a major event
    * Ending weeks/months after the event
 #### Data Analysis
 * Popularity Graphs
 * Word Histograms
 * Hashtag Relevance
 * Top Post Trends
 #### Visualization
 * Matplotlib
 * Bokeh
 * Worldcloud

## Dataset

## Applications

## File Structure
```
Root
|
+-datasets
|  
|
+-scripts
|  |  create_processed_data.py
|  |  word_freq.py
|  |  SQLite.py
|  |  common_words.txt
|  |  Industry_words.txt
|
- ECE_143_Final_Project_Group17.pdf
- main.py
- 
```

## Set Up Instructions

### Required Packages
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. wordcloud

To install packages, type ```sudo pip3 install <packagename>``` on the command line.
