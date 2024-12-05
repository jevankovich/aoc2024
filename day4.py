#!/usr/bin/python3
import sys

def findall(lines: list[str], finger: str) -> int:
	DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
	height = len(lines)
	width = len(lines[0])
	numfound = 0

	for i in range(height):
		for j in range(width):
			for dj, di in DIRS:
				found = True
				try:
					for k, c in enumerate(finger):
						if k * di < -i or k * dj < -j:
							found = False
							break

						if lines[i + k * di][j + k * dj] != c:
							found = False
							break
				except:
					found = False

				if found:
					numfound += 1

	return numfound

def findmas(lines: list[str]) -> int:
	height = len(lines)
	width = len(lines[0])
	numfound = 0

	for i in range(1, height - 1):
		for j in range(1, width - 1):
			if lines[i][j] == 'A':
				posdiag = lines[i - 1][j - 1] + 'A' + lines[i + 1][j + 1]
				negdiag = lines[i - 1][j + 1] + 'A' + lines[i + 1][j - 1]

				if (posdiag == 'MAS' or posdiag == 'SAM') and (negdiag == 'MAS' or negdiag == 'SAM'):
					numfound += 1

	return numfound

def main(lines: list[str]):
	for i in range(len(lines)):
		lines[i] = lines[i].rstrip()

	print(findall(lines, 'XMAS'))
	print(findmas(lines))

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)