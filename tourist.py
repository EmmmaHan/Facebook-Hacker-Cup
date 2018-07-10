#!/usr/bin/python3

import sys

INPUT = open(sys.argv[1])

T = int(INPUT.readline().strip())

for t in range(1, T+1):
	N,K,V = [int(x) for x in INPUT.readline().strip().split(' ')]
	attractions = []
	for _ in range(N):
		attractions.append(INPUT.readline().strip())

	start = ((V-1)*K) % N
	VISIT = []
	items_rest = len(attractions[start:]) 

	if K > items_rest:	#items to add > length of rest of the list
		VISIT.extend(attractions[:(K-items_rest)])	#attractions[0] to the number of items that flow out of range counting from start
		VISIT.extend(attractions[start:])	#rest of the items
	else:				
		while K:
			VISIT.append(attractions[start])
			start += 1
			K -=1

	print('Case #{}: '.format(t) + ' '.join(x for x in VISIT))