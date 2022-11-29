#!/usr/bin/env python
import sys
import json

top_subs = []

if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as file:
        for line in file:
            top_subs.append(line.split(' \t')[0])

    for line in sys.stdin:
        comment = json.loads(line)
        if comment['subreddit'] in top_subs:
            user = comment['author']
            if user not in ['AutoModerator', '[deleted]', 'havoc_bot', 'autowikibot','PRBot', 'PoliticBot']:
              print(comment['subreddit'], '\t', user)

else:
    for line in sys.stdin:
        comment = json.loads(line)
        user = comment['author']
        if user not in ['AutoModerator', '[deleted]', 'havoc_bot', 'autowikibot','PRBot', 'PoliticBot']:
          print(comment['subreddit'], '\t', user)
