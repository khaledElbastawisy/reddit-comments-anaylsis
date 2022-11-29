#!/usr/bin/python3
import sys

for line in sys.stdin:
    subreddit, user, count = line.strip().split('\t')
    print(subreddit, user, count, sep='\t')
