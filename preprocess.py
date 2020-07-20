import spacy
from emoji import demojize
nlp = spacy.load('en')

def emoji_to_text(line):
  line = demojize(line)
  return line
def preprocess(sentence):
  sentence = emoji_to_text(sentence)
  sentence = nlp(sentence)
  sentence = [word for word in sentence if not word.is_punct]
  print(sentence)