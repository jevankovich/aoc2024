#!/usr/bin/python3
from abc import abstractmethod
import sys
from itertools import zip_longest


def interp(a, b, c, prog, debug=False):
	pc = 0

	def combo(rand):
		if rand < 4:
			return rand
		elif rand == 4:
			return a
		elif rand == 5:
			return b
		elif rand == 6:
			return c
		else:
			raise ArithmeticError

	while pc < len(prog):
		op = prog[pc]
		rand = prog[pc + 1]

		str_op = ['adv', 'bxl', 'bst', 'jnz', 'bxc', 'out', 'bdv', 'cdv'][op]
		if debug:
			print(f'{pc}:\t{str_op} {rand} (a: o{a:o}, b: o{b:o}, c: o{c:o})')

		pc += 2

		if op == 0: # adv
			a = a >> combo(rand)
		elif op == 1: # bxl
			b = b ^ rand
		elif op == 2: # bst
			b = 7 & combo(rand)
		elif op == 3: # jnz
			if a != 0: pc = rand
		elif op == 4: # bxc
			b = b ^ c
		elif op == 5: # out
			yield 7 & combo(rand)
		elif op == 6: # bdv
			b = a >> combo(rand)
		elif op == 7: # cdv
			c = a >> combo(rand)


def invert(prog, debug=False):
	# Assumptions:
	# - a is shifted by 3 every iteration
	# - the final instruction is jnz 0
	# - the value of b and c at the start of each iteration doesn't matter

	# We can do this an octal digit at a time
	a = 0
	for dig in range(1, len(prog) + 1):
		a <<= 3
		while True:
			out = list(interp(a, 0, 0, prog))

			if out == prog[-dig:]:
				if debug:
					print(oct(a), out)
				break

			a += 1

	return a


def main(lines: list[str]):
	a = int(lines[0].split()[-1])
	b = int(lines[1].split()[-1])
	c = int(lines[2].split()[-1])

	prog = list(map(int, lines[4].split()[-1].split(',')))

	print(','.join(map(str, interp(a, b, c, prog))))

	a = invert(prog, debug=False)
	print(a)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)