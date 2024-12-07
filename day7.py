#!/usr/bin/python3
import sys

def main(lines: list[str]):
	calibration = 0
	calibration_cat = 0
	for line in lines:
		result, terms = line.split(': ')
		result = int(result)
		terms = list(map(int, terms.split(' ')))

		possible = {terms[0]}
		for term in terms[1:]:
			mul = {x * term for x in possible}
			add = {x + term for x in possible}
			possible = mul | add

		if result in possible:
			calibration += result

		possible_cat = {terms[0]}
		for term in terms[1:]:
			mul = {x * term for x in possible_cat}
			add = {x + term for x in possible_cat}
			cat = {int(str(x) + str(term)) for x in possible_cat}
			possible_cat = mul | add | cat

		if result in possible_cat:
			calibration_cat += result

	print(calibration)
	print(calibration_cat)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)