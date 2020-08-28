# System imports
import re

# External Imports
import pandas as pd
import spacy
from emoji import demojize

# Internal imports
from tweepy_config import COLS

# Intialize the spacy statistical model
nlp = spacy.load('en_core_web_sm')

def emoji_to_text(line):
    """Translate emoji to words as emoji hold important information in twitter

    Args:
        line ([string]): Input sentence with emoji as unicode characters

    Returns:
        [string]: Output sentence with the unicode emoji converted to text
    """

    line = demojize(line)
    return line


def process(sentence):

    """
    Preprocess framework.Peforms the following operation\
        * Convert emoji to root meaning
        * Tokenization and creating a spacy doc
        * Remove punctuation
        * Removes words of less than 3 letters
        * Removes Standard stop words (I'll add a custom set later)
        * Removes urls
        * Reduces each word to its root lemma 

    Returns:
        [string]: Output string after the above preprocessing
    """
    sentence = emoji_to_text(sentence)
    sentence = nlp(sentence)
    
    sentence = [word for word in sentence if not word.is_punct]
    sentence = [word for word in sentence if len(word)>3]
    sentence = [word for word in sentence if not word.is_stop]
    sentence = [word for word in sentence if not word.like_url]
    sentence = [word.lemma_ for word in sentence]
    
    return " ".join(sentence)


def cleaner(tweet):
    """
    Utility Function to serialize the workflow for cleaning up a tweets
    Args:
        tweet (Tweet object): [A tweet object containing all the information realted to a tweet]
    Returns:
        [list]: [List holding a cleaned object information as 
        'id', 'created_at', 'original_text','clean_text', 'retweet_count', 'hashtags','mentions', 'original_author']
    """

    cleaned_tweet = []
    cleaned_text = process(tweet.text)

    cleaned_tweet.append(tweet.id)
    cleaned_tweet.append(tweet.date)
    cleaned_tweet.append(tweet.text)
    cleaned_tweet.append(cleaned_text)
    cleaned_tweet.append(tweet.retweets)


    # Use hashtags and add them to the list
    hashtags = "".join([hashtag_item for hashtag_item in tweet.hashtags])
    hashtags = hashtags if hashtags != '' else '<UNK>'
    cleaned_tweet.append(hashtags.strip())

    # Use mentions .Will be needed later
    mentions = "".join([mention for mention in tweet.mentions])
    mentions = mentions if mentions != '' else '<UNK>'
    cleaned_tweet.append(mentions)


    cleaned_tweet.append(tweet.username)

    return cleaned_tweet
