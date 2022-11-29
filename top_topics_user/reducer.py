#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

users_word_dict = {}
for line in sys.stdin:
  line = line.strip()
  user, word = line.split("\t")
  if (user, word) not in users_word_dict.keys():
    users_word_dict[(user, word)] = 1
  else:
    users_word_dict[(user, word)] += 1

for i in list(users_word_dict.items()):
  print("{}\t{}\t{}".format(i[0][0],i[0][1],i[1]))

