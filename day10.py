#!/usr/bin/python3
import sys

def score(grid, start):
	locs = {start}
	for height in range(1, 10):
		newlocs = set()
		for (x, y) in locs:
			if x > 0                and grid[y][x - 1] == height: newlocs.add((x - 1, y))
			if x < len(grid[y]) - 1 and grid[y][x + 1] == height: newlocs.add((x + 1, y))
			if y > 0                and grid[y - 1][x] == height: newlocs.add((x, y - 1))
			if y < len(grid) - 1    and grid[y + 1][x] == height: newlocs.add((x, y + 1))

		locs = newlocs

	return len(locs)

def trails(grid, start):
	locs = {start: 1}
	for height in range(1, 10):
		newlocs = {}
		for (x, y), paths in locs.items():
			if x > 0                and grid[y][x - 1] == height: newlocs[(x - 1, y)] = newlocs.get((x - 1, y), 0) + paths
			if x < len(grid[y]) - 1 and grid[y][x + 1] == height: newlocs[(x + 1, y)] = newlocs.get((x + 1, y), 0) + paths
			if y > 0                and grid[y - 1][x] == height: newlocs[(x, y - 1)] = newlocs.get((x, y - 1), 0) + paths
			if y < len(grid) - 1    and grid[y + 1][x] == height: newlocs[(x, y + 1)] = newlocs.get((x, y + 1), 0) + paths

		locs = newlocs

	return sum(locs.values())

def main(lines: list[str]):
	grid = []
	starts = []
	for y, line in enumerate(lines):
		row = []
		for x, c in enumerate(line.strip()):
			height = int(c)
			row.append(height)

			if height == 0:
				starts.append((x,y))

		grid.append(row)

	total_score = 0
	total_trails = 0
	for start in starts:
		total_score += score(grid, start)
		total_trails += trails(grid, start)

	print(total_score)
	print(total_trails)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)