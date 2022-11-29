#!/usr/bin/env python
import sys
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

top_users = []
sentiment = SentimentIntensityAnalyzer()
if len(sys.argv) > 1:
  with open(sys.argv[1], "r") as file:
      for line in file:
          top_users.append(line.split(' \t')[0])

  for line in sys.stdin:
      comment = json.loads(line)
      if comment['author'] in top_users:
        body = comment['body']
        if body != '[deleted]':
            attitude_dict = sentiment.polarity_scores(body)
            neg, neu, pos, _ = list(attitude_dict.values())
            print(comment['author'], '\t', pos, '\t', neg)

else:
  for line in sys.stdin:
      comment = json.loads(line)
      if comment['author'] not in ['AutoModerator', '[deleted]', 'havoc_bot', 'autowikibot', 'PRBot', 'PoliticBot']:
        body = comment['body']
        if body != '[deleted]':
            attitude_dict = sentiment.polarity_scores(body)
            neg, neu, pos, _ = list(attitude_dict.values())
            print(comment['author'], '\t', pos, '\t', neg)
