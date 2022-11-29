#!/usr/bin/python3
import sys
import json

for line in sys.stdin:
    comment = json.loads(line)
    print(comment['subreddit'],"\t1")

