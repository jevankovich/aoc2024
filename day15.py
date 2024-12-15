#!/usr/bin/python3
import sys

def show_warehouse(warehouse: list[list[int]], robot: tuple[int, int]):
	for y, row in enumerate(warehouse):
		for x, a in enumerate(row):
			print('#' if a == 2 else 'O' if a == 1 else '@' if (x, y) == robot else '.', end='')
		print()

def move(warehouse: list[list[int]], robot: tuple[int, int], dx: int, dy: int) -> tuple[int, int]:
	x, y = robot

	l = 1
	while warehouse[y + l*dy][x + l*dx] == 1:
		l += 1

	if warehouse[y + l*dy][x + l*dx] == 2:
		# wall stops us
		return robot

	# Can push
	warehouse[y + dy][x + dx] = 0
	for i in range(2, l + 1):
		warehouse[y + i*dy][x + i*dx] = 1

	return x + dx, y + dy

def partone(lines: list[str]):
	warehouse = []
	instructions = 0
	robot = (0, 0)
	for i, line in enumerate(lines):
		if line == '\n':
			instructions = i + 1
			break

		row = list(map(lambda c: 2 if c == '#' else 1 if c == 'O' else 0, line.strip()))
		warehouse.append(row)

		if '@' in line:
			robot = (i, line.index('@'))

	# show_warehouse(warehouse, robot)
	# print()

	for line in lines[instructions:]:
		for c in line:
			dx = 0
			dy = 0
			if c == '<':
				dx = -1
			elif c == '>':
				dx = 1
			elif c == '^':
				dy = -1
			elif c == 'v':
				dy = 1
			else:
				continue

			robot = move(warehouse, robot, dx, dy)
			# show_warehouse(warehouse, robot)
			# print()

	gps = 0
	for y, row in enumerate(warehouse):
		for x, a in enumerate(row):
			if a == 1:
				gps += 100 * y + x

	print(gps)

def show_big_warehouse(warehouse, robot):
	for y, row in enumerate(warehouse):
		for x, a in enumerate(row):
			if a == 3:
				s = '#'
			elif a == 2:
				s = ']'
			elif a == 1:
				s = '['
			elif (x, y) == robot:
				s = '@'
			else:
				s = '.'
			print(s, end='')
		print()

def big_move(warehouse, robot, dx, dy):
	x, y = robot

	if dy:
		# Harder case, consider half-boxes hitting other half-boxes
		wall = False
		xss = [[x]]
		while True:
			new_xs = []
			for x in xss[-1]:
				if warehouse[y + len(xss)*dy][x] == 3:
					wall = True
					new_xs = []
					break
				elif warehouse[y + len(xss)*dy][x] == 2:
					if x - 1 not in xss[-1]:
						new_xs.extend((x - 1, x))
				elif warehouse[y + len(xss)*dy][x] == 1:
					new_xs.extend((x, x + 1))

			if not new_xs:
				break
			xss.append(new_xs)

		if wall:
			# Hit a wall, no change
			return robot

		for i in range(len(xss) - 1, -1, -1):
			xs = xss[i]
			for x in xs:
				warehouse[y + (i+1)*dy][x] = warehouse[y + i*dy][x]
				warehouse[y + i*dy][x] = 0
	else:
		l = 1
		while warehouse[y][x + l*dx] in (1,2):
			l += 1

		if warehouse[y][x + l*dx] == 3:
			# wall stops us
			return robot

		# Can push
		for i in range(l - 1, -1, -1):
			warehouse[y][x + (i+1)*dx] = warehouse[y][x + i*dx]
			warehouse[y][x + i*dx] = 0

	return x + dx, y + dy


def parttwo(lines: list[str]):
	warehouse = []
	instructions = 0
	robot = (0, 0)
	for y, line in enumerate(lines):
		if line == '\n':
			instructions = y + 1
			break

		row = []
		for x, c in enumerate(line.strip()):
			if c == '#':
				row.extend([3, 3])
			elif c == 'O':
				row.extend([1, 2])
			else:
				row.extend([0, 0])
				if c == '@':
					robot = (2*x, y)

		warehouse.append(row)

	# show_big_warehouse(warehouse, robot)
	# print()

	for line in lines[instructions:]:
		for c in line:
			dx = 0
			dy = 0
			if c == '<':
				dx = -1
			elif c == '>':
				dx = 1
			elif c == '^':
				dy = -1
			elif c == 'v':
				dy = 1
			else:
				continue

			robot = big_move(warehouse, robot, dx, dy)
			# show_big_warehouse(warehouse, robot)
			# print()

	gps = 0
	for y, row in enumerate(warehouse):
		for x, a in enumerate(row):
			if a == 1:
				gps += 100 * y + x

	print(gps)

def main(lines: list[str]):
	partone(lines)
	parttwo(lines)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)