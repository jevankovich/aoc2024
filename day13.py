#!/usr/bin/python3
import sys
import math

def euclid(a, b):
	s0, s1 = 1, 0
	t0, t1 = 0, 1

	while b != 0:
		q, r = divmod(a, b)
		a, b = b, r
		s0, s1 = s1, s0 - q * s1
		t0, t1 = t1, t0 - q * t1

	return a, s0, t0


def mintokens(ax, ay, bx, by, px, py):
	# Compute the number of a's and b's to add to change the x position by step
	# Matrix form:
	# [ ax bx | px ]
	# [ ay by | py ]
	#
	# Partially reducing:
	# [ ax by - ay bx  0  |  px by - py bx ]
	# [ ay             by |  py ]
	a, rem = divmod(px * by - py * bx, ax * by - ay * bx)
	if rem != 0:
		return None

	b, rem = divmod(py - a * ay, by)
	if rem != 0:
		return None

	return 3*a + b


def main(lines: list[str]):
	tottokens = 0
	fartokens = 0
	for i in range(0, len(lines), 4):
		_, _, ax, ay = lines[i].split()
		_, _, bx, by = lines[i + 1].split()
		_, px, py = lines[i + 2].split()

		ax = int(ax.removeprefix('X+').removesuffix(','))
		ay = int(ay.removeprefix('Y+'))

		bx = int(bx.removeprefix('X+').removesuffix(','))
		by = int(by.removeprefix('Y+'))

		px = int(px.removeprefix('X=').removesuffix(','))
		py = int(py.removeprefix('Y='))

		toks = mintokens(ax, ay, bx, by, px, py)
		if toks is not None:
			tottokens += toks

		toks = mintokens(ax, ay, bx, by, 10000000000000 + px, 10000000000000 + py)
		if toks is not None:
			fartokens += toks

	print(tottokens)
	print(fartokens)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)