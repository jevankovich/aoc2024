#!/usr/bin/python3
import sys

def main():
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	print(lines[0])

if __name__ == '__main__':
	main()