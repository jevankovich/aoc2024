#!/usr/bin/python3
import sys

def walk(guard, obstructions, width, height, dx=0, dy=-1):
	while 0 <= guard[0] < width and 0 <= guard[1] < height:
		nextpos = (guard[0] + dx, guard[1] + dy)

		if nextpos in obstructions:
			dx, dy = -dy, dx
			continue

		# print(guard, '->', nextpos)
		yield guard, nextpos
		guard = nextpos

def doesloop(guard, dx, dy, obstructions, width, height):
	hit = set()

	while 0 <= guard[0] < width and 0 <= guard[1] < height:
		nextpos = (guard[0] + dx, guard[1] + dy)

		if nextpos in obstructions:
			if (nextpos, dx, dy) in hit:
				return True
			hit.add((nextpos, dx, dy))
			dx, dy = -dy, dx
			continue

		guard = nextpos
	
	return False
			

def countloops(guard, obstructions, width, height):
	loops = 0
	tried = set()
	for g, n in walk(guard, obstructions, width, height):
		dx = n[0] - g[0]
		dy = n[1] - g[1]

		if n in tried:
			continue
		tried.add(n)

		obstructions.add(n)
		if doesloop(g, dx, dy, obstructions, width, height):
			loops += 1
		obstructions.remove(n)


	return loops
	

def main(lines: list[str]):
	height = len(lines)
	width = len(lines[0]) - 1

	obstructions = set()
	guard = (0, 0)
	for y in range(height):
		for x in range(width):
			c = lines[y][x]
			if c == '#':
				obstructions.add((x,y))
			elif c == '^':
				guard = (x, y)
	
	visited = {guard for guard, _ in walk(guard, obstructions, width, height)}
	print(len(visited))
	print(countloops(guard, obstructions, width, height))


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)
