#!/usr/bin/python3
import sys


def safe(report: list[int]):
	diff = list(map(lambda x, y: x - y, report[:-1], report[1:]))
	l = min(diff)
	h = max(diff)
	return (l >= 1 and h <= 3) or (l >= -3 and h <= -1)


def trial_dampen(report: list[int]):
	for i in range(len(report)):
		if safe(report[:i] + report[i+1:]):
			return True

	return False

def main(lines: list[str]):
	reports = []
	for line in lines:
		reports.append(list(map(int, line.split())))

	numsafe = 0
	dampsafe = 0
	for report in reports:
		diff = list(map(lambda x, y: x - y, report[:-1], report[1:]))
		l = min(diff)
		h = max(diff)
		if (l >= 1 and h <= 3) or (l >= -3 and h <= -1):
			numsafe += 1
		elif trial_dampen(report):
			dampsafe += 1

	print(numsafe)
	print(numsafe + dampsafe)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)