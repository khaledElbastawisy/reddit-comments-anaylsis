#!/usr/bin/python3
import sys
import json

for line in sys.stdin:
    comment = json.loads(line)
    if comment['author'] not in ['AutoModerator', '[deleted]', 'havoc_bot', 'autowikibot','PRBot', 'PoliticBot']:
      print(comment['author'],"\t1")

