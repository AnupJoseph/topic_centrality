import spacy
import re
from emoji import demojize
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
  return " ".join(sentence)
