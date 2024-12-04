#!/usr/bin/python3
import sys
import re

def main(lines: list[str]):
	enabled = True
	total = 0
	total_conditional = 0
	for line in lines:
		for match in re.finditer(r"mul\((\d*),(\d*)\)|do\(\)|don't\(\)", line):
			if match[0].startswith('don'):
				enabled = False
			elif match[0].startswith('do'):
				enabled = True
			else:
				x = int(match[1])
				y = int(match[2])
				total += x * y
				if enabled:
					total_conditional += x * y

	print(total)
	print(total_conditional)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)