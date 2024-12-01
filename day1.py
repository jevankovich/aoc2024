#!/usr/bin/python3
import sys

def main(lines: list[str]):
	left = []
	right = []
	for line in lines:
		l, r = line.split()
		left.append(int(l))
		right.append(int(r))

	left.sort()
	right.sort()

	total_dist = 0
	for l, r in zip(left, right):
		total_dist += l - r if l > r else r - l

	print(total_dist)

	similarity = 0
	for l in left:
		similarity += l * right.count(l)

	print(similarity)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)