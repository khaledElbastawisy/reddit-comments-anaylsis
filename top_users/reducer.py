import sys
users = {}
N = int(sys.argv[1])
for line in sys.stdin:
	line = line.strip()
	userid, count = line.split("\t")
	count = int(count)
	if userid not in users.keys():
		users[userid] = 1
	else: users[userid] += count
sortedusers = {r: users[r] for r in sorted(users, key=users.get, reverse=True)}
for i in list(sortedusers.items())[:N]:
	print("{}\t{}".format(i[0],i[1]))

