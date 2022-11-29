import sys
subs = {}
N = int(sys.argv[1])
for line in sys.stdin:
	line = line.strip()
	subid, count = line.split("\t")
	if subid not in subs.keys():
		subs[subid] = 1
	else:
    		subs[subid] = subs[subid] + int(count)
sortedsubs = {r: subs[r] for r in sorted(subs, key=subs.get, reverse=True)}
for i in list(sortedsubs.items())[:N]:
	print("{}\t{}".format(i[0],i[1]))

