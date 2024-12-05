#!/usr/bin/python3
import sys
import functools

def compare(order: dict[str, set[str]]):
	def _compare(s1: str, s2: str) -> int:
		if s1 in order:
			if s2 in order[s1]:
				return -1
		
		if s2 in order:
			if s1 in order[s2]:
				return 1

		return 0
	
	return _compare

def main(lines: list[str]):
	order: dict[str, set[str]] = dict()

	for i, line in enumerate(lines):
		line = line.strip()
		if line == "":
			break
	
		before, after = line.split('|')

		if before in order:
			order[before].add(after)
		else:
			order[before] = {after}
	
	middlesum = 0
	fixedsum = 0
	for line in lines[i+1:]:
		line = line.strip()
		update = line.split(',')

		ordered = True
		seen = set()
		for page in update:
			if order.get(page, set()) & seen:
				ordered = False
				break
			
			seen.add(page)

		if ordered:
			middlesum += int(update[len(update) // 2])

		else:
			fixed = sorted(update, key=functools.cmp_to_key(compare(order)))

			fixedsum += int(fixed[len(update) // 2])
	
	print(middlesum)
	print(fixedsum)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)
