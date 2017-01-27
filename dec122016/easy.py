import sys;

wordfile = sys.argv[1]

with open(wordfile, 'r') as words:
	start = list(words.readline())
	finish = list(words.readline())
	
for i in range(len(start)):
	if (start[i] != finish[i]):
		print "".join(finish[:i] + start[i:]).strip("\n")
	start[i] = finish[i]

print "".join(finish).strip("\n")
