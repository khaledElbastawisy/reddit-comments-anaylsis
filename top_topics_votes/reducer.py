#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

N = int(sys.argv[1])
topics_up_dict = {}
for line in sys.stdin:
  line = line.strip()
  topic, upvote = line.split("\t")
  upvote = int(upvote)
  if topic not in topics_up_dict.keys():
    topics_up_dict[topic] = upvote
  else:
    topics_up_dict[topic] = topics_up_dict[topic] + upvote

sortedtopics= {r: topics_up_dict[r] for r in sorted(topics_up_dict, key=topics_up_dict.get, reverse=True)}

for i in list(sortedtopics.items())[:N]:
  print("{}\t{}".format(i[0],i[1]))

