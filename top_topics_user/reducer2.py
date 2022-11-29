#!/usr/bin/python3
import sys
first_line = sys.stdin.readline()
curr_user , max_topic, max_count = first_line.strip().split('\t')
max_count = int(max_count)
for line in sys.stdin:
  new_user, new_topic, new_count = line.strip().split('\t')
  new_count = int(new_count)

  if curr_user == new_user:
    if new_count > max_count:
      max_count = new_count
      max_topic = new_topic
  else:
    print('{}\t{}\t{}'.format(curr_user, max_topic, max_count))
    curr_user, max_topic, max_count = new_user, new_topic, new_count

