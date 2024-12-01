#!/usr/bin/python3
import sys

def main(lines: list[str]):
	print(lines[0].rstrip())

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)