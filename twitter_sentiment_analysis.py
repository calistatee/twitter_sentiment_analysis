import tweepy
import csv
from urlextract import URLExtract
from textblob import TextBlob

# log in via codes provided by Twitter
consumer_key = 'enter your consumer key'
consumer_secret = 'enter your consumer secret key'

access_token = 'enter your access token'
access_token_secret = 'enter your access token secret'

# this is for authentication by using OAuthHandler and set_access_token method
# from tweepy with a bunch of codes hidden to us
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# main variables where we'll do all the twitter magic
api = tweepy.API(auth)

# now, we want to search for tweets

# create a public var to store a list of tweets
# .search method will retrieve a bunch of tweets with the designated word (MeToo)
public_tweets = api.search('MeToo')

# to export to .csv
# 'with open' helps close your file automatically
with open('twitter_sentiment_analysis.csv', 'w', newline = '') as output:

    # create var
    fileOut = csv.writer(output)
    data = [['Tweets', 'Polarity', 'Subjectivity', 'URL']]

    fileOut.writerows(data)

    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        # default value for url
        # if url = None, perform operations on tweet.text to cut off existing url
        url = None

        # to start a separate column for URL
        # split texts into chunks
        words = tweet.text.split()

        # to extract link...
        link = URLExtract()

        # find links within a tweet
        urls = link.find_urls(tweet.text)

        # identify link - http / https (http is common denominator for both)
        for word in words:
            #print (word)
            if 'http' in word:
                url = word
                
        fileOut.writerow([tweet.text, polarity, subjectivity, url])

        # print to terminal
        print (tweet.text)
        print ('Polarity: ', polarity)
        print ('Subjectivity:', subjectivity)
        
 # check your CSV file for clean results!
