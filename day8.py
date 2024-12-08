#!/usr/bin/python3
import sys

def main(lines: list[str]):
	height = len(lines)
	width = len(lines[0].strip())

	antennas = dict()

	for y, line in enumerate(lines):
		line = line.strip()
		for x, c in enumerate(line):
			if c == '.':
				continue

			if c not in antennas:
				antlist = []
				antennas[c] = antlist
			else:
				antlist = antennas[c]

			antlist.append((x, y))

	antinodes = set()
	more_antinodes = set()
	for antlist in antennas.values():
		for i, (x1, y1) in enumerate(antlist):
			for x2, y2 in antlist[i+1:]:
				dx = x2 - x1
				dy = y2 - y1
				# print(x1, x2, dx)
				# print(y1, y2, dy)

				antix1 = x2 + dx
				antiy1 = y2 + dy

				antix2 = x1 - dx
				antiy2 = y1 - dy

				if 0 <= antix1 < width and 0 <= antiy1 < height:
					# print(antix1, antiy1)
					antinodes.add((antix1, antiy1))

				if 0 <= antix2 < width and 0 <= antiy2 < height:
					# print(antix2, antiy2)
					antinodes.add((antix2, antiy2))

				x = x2
				y = y2
				while 0 <= x < width and 0 <= y < height:
					more_antinodes.add((x, y))
					x += dx
					y += dy

				x = x1
				y = y1
				while 0 <= x < width and 0 <= y < height:
					more_antinodes.add((x, y))
					x -= dx
					y -= dy

	print(len(antinodes))
	print(len(more_antinodes))

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)