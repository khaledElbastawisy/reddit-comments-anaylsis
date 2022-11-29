#!/usr/bin/python3
import sys

for line in sys.stdin:
    subreddit, topic, count = line.strip().split('\t')
    print(subreddit, topic, count, sep='\t')
