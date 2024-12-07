#!/usr/bin/python3
import sys

def possible(result, terms, cat=False):
	results = {result}
	for term in reversed(terms[1:]):
		next_results = set()
		for result in results:
			if result > term:
				next_results.add(result - term)

			if result % term == 0:
				next_results.add(result // term)

			if cat:
				sresult = str(result)
				sterm = str(term)
				if len(sresult) > len(sterm) and sresult.endswith(sterm):
					next_results.add(int(sresult.removesuffix(sterm)))

		results = next_results

	return terms[0] in results


def main(lines: list[str]):
	calibration = 0
	calibration_cat = 0
	for line in lines:
		result, terms = line.split(': ')
		result = int(result)
		terms = list(map(int, terms.split(' ')))

		if possible(result, terms):
			calibration += result

		if possible(result, terms, True):
			calibration_cat += result

	print(calibration)
	print(calibration_cat)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)