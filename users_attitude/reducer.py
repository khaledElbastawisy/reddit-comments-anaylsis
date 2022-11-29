#!/usr/bin/python3
import sys
first_line = sys.stdin.readline()
curr_user , curr_pos, curr_neg = first_line.strip().split('\t')
curr_pos = float(curr_pos)
curr_neg = float(curr_neg)
user_pos = curr_pos
user_neg = curr_neg
for line in sys.stdin:
  new_user, new_pos, new_neg = line.strip().split('\t')
  new_pos = float(new_pos)
  new_neg = float(new_neg)

  if curr_user == new_user:
    user_pos += new_pos
    user_neg += new_neg

  else:
    if user_neg == 0: user_neg == 0.01
    print('{}\t{}'.format(curr_user, user_pos/user_neg))
    curr_user, curr_pos, curr_neg = new_user, new_pos, new_neg
    user_pos = curr_pos
    user_neg = curr_neg