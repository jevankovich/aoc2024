#!/usr/bin/python3
import sys

def main(lines: list[str], width: int = 101, height: int = 103):
	q1, q2, q3, q4 = 0, 0, 0, 0
	bots = []
	start = set()
	for line in lines:
		p, v = line.split()
		x, y = map(int, p.removeprefix('p=').split(','))
		vx, vy = map(int, v.removeprefix('v=').split(','))

		bots.append((x, y, vx, vy))
		start.add((x, y))

		x = (x + 100*vx) % width
		y = (y + 100*vy) % height

		if x < width // 2:
			if y < height // 2:
				q1 += 1
			elif y > height // 2:
				q2 += 1
		elif x > width // 2:
			if y < height // 2:
				q3 += 1
			elif y > height // 2:
				q4 += 1

	print(q1 * q2 * q3 * q4)

	t = 1
	while True:
		end = set()
		for x, y, vx, vy in bots:
			x = (x + t*vx) % width
			y = (y + t*vy) % height

			end.add((x, y))

		# Search for top of Christmas tree
		top = False
		for i in range(height - 1):
			for j in range(1, width - 1):
				if (j, i) in end and (j - 1, i + 1) in end and (j, i + 1) in end and (j + 1, i + 1) in end and (j - 2, i + 2) in end and (j - 1, i + 2) in end and (j, i + 2) in end and (j + 1, i + 2) in end and (j + 2, i + 2) in end:
					top = True
					break

			if top:
				break

		if top:
			print(t)

			if False:
				for i in range(height):
					for j in range(width):
						if (j, i) in end:
							print('#', end='')
						elif i == height // 2 or j == width // 2:
							print('~', end='')
						else:
							print(' ', end='')

					print('|')
				print()

			break

		if end == start:
			break

		t += 1

if __name__ == '__main__':
	width = 101
	height = 103
	if sys.argv[1].endswith('_example.txt'):
		width = 11
		height = 7

	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines, width, height)