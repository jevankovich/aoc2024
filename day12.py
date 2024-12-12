#!/usr/bin/python3
import sys

def flood(grid, x, y):
	plant = grid[y][x]
	explore = {(x, y)}
	seen = {(x, y)}
	fences = set()
	while explore:
		next_explore = set()
		for x, y in explore:
			if grid[y][x - 1] == plant: next_explore.add((x - 1, y))
			else: fences.add((x, y, -1, 0))

			if grid[y][x + 1] == plant: next_explore.add((x + 1, y))
			else: fences.add((x, y, +1, 0))

			if grid[y - 1][x] == plant: next_explore.add((x, y - 1))
			else: fences.add((x, y, 0, -1))

			if grid[y + 1][x] == plant: next_explore.add((x, y + 1))
			else: fences.add((x, y, 0, +1))

		explore = next_explore - seen
		seen.update(explore)

	return seen, fences


def edges(fences):
	segs = 0
	while fences:
		segs += 1
		x, y, nx, ny = fences.pop()
		# Walk in both orthogonal directions, and remove all fences that are adjacent
		xx = x - ny
		yy = y + nx
		while (xx, yy, nx, ny) in fences:
			fences.remove((xx, yy, nx, ny))
			xx -= ny
			yy += nx

		xx = x + ny
		yy = y - nx
		while (xx, yy, nx, ny) in fences:
			fences.remove((xx, yy, nx, ny))
			xx += ny
			yy -= nx

	return segs


def main(lines: list[str]):
	grid = []
	for line in lines:
		row = ' ' + line.strip() + ' '
		grid.append(row)

	grid.insert(0, ' ' * len(grid[0]))
	grid.append(' ' * len(grid[0]))

	height = len(grid) - 2
	width = len(grid[0]) - 2

	regions = {}
	roots = {}

	price = 0
	bulkprice = 0
	for y in range(1, height + 1):
		for x in range(1, width + 1):
			if (x, y) not in roots:
				region, fences = flood(grid, x, y)
				regions[(x,y)] = region
				for xy in region:
					roots[xy] = (x, y)

				price += len(region) * len(fences)

				segs = edges(fences)
				bulkprice += len(region) * segs


	print(price)
	print(bulkprice)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)