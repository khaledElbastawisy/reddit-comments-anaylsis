#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

subs_usr_dict = {}
for line in sys.stdin:
    line = line.strip()
    subreddit, user = line.split("\t")
    if (subreddit, user) not in subs_usr_dict.keys():
        subs_usr_dict[(subreddit, user)] = 1
    else:
        subs_usr_dict[(subreddit, user)] = subs_usr_dict[(subreddit, user)] + 1

for i in list(subs_usr_dict.items()):
    print("{}\t{}\t{}".format(i[0][0], i[0][1], i[1]))
