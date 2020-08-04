import spacy
import re
from emoji import demojize
nlp = spacy.load('en')

def emoji_to_text(line):
  """Translate emoji to words as emoji hold infomration in tittwe
  
  Args:
      line (String): Sentence for preprocessing
  
  Returns:
      string: Sentence with emoji cleared 
  """
  line = demojize(line)
  return line

def remove_url(sentence):
	"""Remove the token
	
	Args:
	    sentence (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	return re.sub(r"http\S+", "", sentence)

def preprocess(sentence):
  """Preprocess framework
  
  Args:
      sentence (String): Input String 
  
  Returns:
      TYPE: Output string
  """
  sentence = emoji_to_text(sentence)
  sentence = nlp(sentence)
  # sentence = [remove_url(str(word.text)) for word in sentence]
  sentence = [word for word in sentence if not word.is_punct]
  sentence = [word for word in sentence if len(word)>3]
  sentence = [word for word in sentence if not word.is_stop]
  sentence = [word.lemma_ for word in sentence]
  # sentence = [remove_url(word) for word in sentence]
  return " ".join(sentence)
