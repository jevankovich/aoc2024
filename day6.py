#!/usr/bin/python3
import sys

def path(start, obstructions, width, height):
	guard = start

	dx = 0
	dy = -1
	visited = set()
	hit = set()
	escapes = False

	while 0 <= guard[0] < width and 0 <= guard[1] < height:
		visited.add(guard)

		nextpos = (guard[0] + dx, guard[1] + dy)

		if nextpos in obstructions:
			if (nextpos, dx, dy) in hit:
				# We've already hit this obstacle from this side, thus we've looped
				return False, visited

			hit.add((nextpos, dx, dy))
			tmp = dx
			dx = -dy
			dy = tmp
			continue

		# print(guard, '->', nextpos)
		guard = nextpos
	
	return True, visited

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
	
	_, visited = path(guard, obstructions, width, height)
	print(len(visited))

	visited.remove(guard)
	loops = 0
	for loc in visited:
		trial_obs = obstructions | {loc}
		escape, _ = path(guard, trial_obs, width, height)
		if not escape:
			loops += 1
	
	print(loops)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)
