#!/usr/bin/python3
import sys
import heapq

def dict_append(d, k, v):
	try:
		d[k].append(v)
	except KeyError:
		d[k] = [v]

def shortest_path(walls, start, end, move_weight=1, turn_weight=1000):
	paths = {}
	frontier = [(0, start, 1, 0, set())]

	shortest = None

	while frontier:
		distance, pos, dx, dy, acc_path = heapq.heappop(frontier)

		if shortest and distance > shortest:
			break
		if pos == end:
			shortest = distance

		key = (pos, dx, dy)
		if key not in paths or paths[key][0] > distance:
			paths[key] = (distance, acc_path)
		elif paths[key][0] == distance:
			_, old_path = paths[key]
			paths[key] = (distance, old_path | acc_path)
		else:
			continue

		# Can turn left, right, or move forward
		x, y = pos
		if (x + dx, y + dy) not in walls:
			heapq.heappush(frontier, (distance + move_weight, (x + dx, y + dy), dx, dy, acc_path | {pos}))
		heapq.heappush(frontier, (distance + turn_weight, pos, -dy, dx, acc_path))
		heapq.heappush(frontier, (distance + turn_weight, pos, dy, -dx, acc_path))

	seats = {end}
	for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		seats |= paths.get((end, dx, dy), (None, set()))[1]

	return shortest, seats


def main(lines: list[str]):
	walls = set()
	start = (0,0)
	end = (0,0)

	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == '#':
				walls.add((x,y))
			elif c == 'S':
				start = (x, y)
			elif c == 'E':
				end = (x, y)

	shortest, seats = shortest_path(walls, start, end)
	print(shortest)

	print(len(seats))


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)