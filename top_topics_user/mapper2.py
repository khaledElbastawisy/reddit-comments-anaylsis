#!/usr/bin/python3
import sys

for line in sys.stdin:
    user, topic, count = line.strip().split('\t')
    print(user, topic, count, sep='\t')
