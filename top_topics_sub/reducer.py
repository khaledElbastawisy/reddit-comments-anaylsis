#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

subs_word_dict = {}
for line in sys.stdin:
  line = line.strip()
  subreddit, word = line.split("\t")
  if (subreddit, word) not in subs_word_dict.keys():
    subs_word_dict[(subreddit, word)] = 1
  else:
    subs_word_dict[(subreddit, word)] = subs_word_dict[(subreddit, word)] + 1

for i in list(subs_word_dict.items()):
  print("{}\t{}\t{}".format(i[0][0],i[0][1],i[1]))

