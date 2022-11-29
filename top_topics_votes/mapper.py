#!/usr/bin/env python
import sys
import json
import re
import nltk
from textblob import TextBlob
from collections import Counter
nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download("wordnet")
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
stops_dict = Counter(stopwords.words('english'))
regex = r"\(?(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})\)?|[^a-z ]"

upordown = int(sys.argv[1])
for line in sys.stdin:
  comment = json.loads(line)
  body = comment['body']
  topics_token = nltk.word_tokenize(body)
  topics_list = [word for (word, pos) in nltk.pos_tag(topics_token) if(pos[:2] == 'NN')]
  if len(topics_list) > 0:
    for topic in topics_list:
      topic = re.sub(regex, "", topic)
      tokens = topic.split(' ')
      for t in tokens:
        if t in stops_dict:
          tokens.remove(t)
      topic = ' '.join(tokens)
      if upordown == 0:
        if len(topic) > 0 and comment['ups'] > 0:
          print(topic, '\t', comment['ups'])
      else:
        if len(topic) > 0 and comment['downs'] > 0:
          print(topic, '\t', comment['downs'])



