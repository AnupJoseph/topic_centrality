import spacy
import re
from emoji import demojize
from tweet_config import COLS
import pandas as pd
nlp = spacy.load('en_core_web_sm')

def emoji_to_text(line):
  """Translate emoji to words as emoji hold infomration in tittwe
  
  Args:
      line (String): Sentence for preprocessing
  
  Returns:
      string: Sentence with emoji cleared 
  """
  line = demojize(line)
  return line


def preprocess(sentence):
  """Preprocess framework.Peforms the following operation\

  * Convert emoji to root meaning
  * Tokenization and creating a spacy doc
  * Remove punctuation
  * Removes words of less than 3 letters
  * Removes Standard stop words (I'll add a custom set later)
  * Removes urls
  * Reduces each word to its root lemma 
  
  Args:
      sentence (String): Input String 
  
  Returns:
      TYPE: Output string after the above preprocessing 
  """
  sentence = emoji_to_text(sentence)
  sentence = nlp(sentence)
  # sentence = [remove_url(str(word.text)) for word in sentence]
  sentence = [word for word in sentence if not word.is_punct]
  sentence = [word for word in sentence if len(word)>3]
  sentence = [word for word in sentence if not word.is_stop]
  sentence = [word for word in sentence if not word.like_url]
  sentence = [word.lemma_ for word in sentence]
#   print(sentence)
  return " ".join(sentence)


def cleaner(tweet):
    cleaned_tweet = []
    tweet = tweet._json
    cleaned_text = preprocess(tweet['full_text'])

    cleaned_tweet 	+= [tweet['id'],'tweet', tweet['created_at'],tweet['source'], tweet['full_text'],cleaned_text,tweet['favorite_count'], tweet['retweet_count']]
    # Use hashtags
    # print(cleaned_tweet)
    hashtags = ",".join([hashtag_item['text'] for hashtag_item in tweet['entities']['hashtags']])
    cleaned_tweet.append(hashtags)

    # Use mentions .Will be needed later
    mentions = ",".join([mention['screen_name'] for mention in tweet['entities']['user_mentions']])
    cleaned_tweet.append(mentions)

    cleaned_tweet.append(tweet['user']['screen_name'])
    single_tweet_df = pd.DataFrame([cleaned_tweet], columns=COLS)
    return single_tweet_df