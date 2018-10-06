#!/usr/bin/python3
#author: Emma Han

import sys

INPUT = open(sys.argv[1])
T = int(INPUT.readline().strip())

for t in range(1, T+1):
	N = int(INPUT.readline().strip())

	if N%2 == 0:
		print('Case #{}: '.format(t) + str(0))	
	else:
		print('Case #{}: '.format(t) + str(1))
		print(float(0))

	for _ in range(N+1):
		INPUT.readline()
		
