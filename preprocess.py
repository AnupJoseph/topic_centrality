import spacy
from emoji import demojize
nlp = spacy.load('en_core_web_lg')
# stopwords = nlp.Defaults.stop_words
# print(stopwords)
def emoji_to_text(line):
  line = demojize(line)
  return line
def preprocess(sentence):
  sentence = emoji_to_text(sentence)
  sentence = nlp(sentence)
  sentence = [word for word in sentence if not word.is_punct]
  sentence = [word for word in sentence if len(word)>3]
  sentence = [word for word in sentence if not word.is_stop]
  sentence = [word.lemma_ for word in sentence]
  
  return sentence
sent = preprocess("Wherever the maple leaf flies, it represents our ric'h history, our bright future, and the values that hold dear as Canadians.Happy flag day 🇨🇦")
print(sent)