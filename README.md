# Hashtags of Major Events (Group 17)

## Team Members
 - Gates Zeng (@gateszeng)
 - Wei-Cheng Huang (@tommyhuangtw)
 - Yayu Lin (@yayul)

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
 * Tweets using top hashtags from five major events
   * MeToo
   * Falcon Heavy Launch
   * Royal Wedding
   * Camp Fire
   * Parkland Shooting
 * Information included
   * Username 
   * User handle
   * Date
   * Number of retweets
   * Number of favorites
   * Text
   * Mentions
   * Hashtags
   * Tweet id
   * Link
## Applications
 * Offering insight into whether a trend would blow up or disappear quickly
 * Designing suitable hashtags for attracting attention
 * Evaluating public opinion on specific events 
## File Structure
```
Root
|
+-datasets
|
|- ECE_143_Final_Project_Group17.pdf
|- plot_frequency_graphs.py
|- analysis_frequency.py
|- Hashtag_text_relevance.py
|- Popular_tweets.py
|- hashtag_trends_visualizations.ipynb
```

## Required Packages
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. wordcloud
6. nltk
7. bokeh

To install packages, type ```sudo pip3 install <packagename>``` on the command line.
