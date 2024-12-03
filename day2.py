#!/usr/bin/python3
import sys


def safe(report: list[int]):
	diff = list(map(lambda x, y: x - y, report[:-1], report[1:]))
	l = min(diff)
	h = max(diff)
	return (l >= 1 and h <= 3) or (l >= -3 and h <= -1)


def dampen(report: list[int]):
	sign = 1 if report[-1] > report[1] else -1
	diff = list(map(lambda x, y: sign * (y - x), report[:-1], report[1:]))
	l = min(diff)
	h = max(diff)
	if l >= 1 and h <= 3:
		return True

	il = diff.index(l)
	ih = diff.index(h)

	if l <= 0:
		# try removing at il and il + 1
		if safe(report[:il] + report[il+1:]) or safe(report[:il+1] + report[il+2:]):
			return True

	if h >= 3:
		# try removing at ih and ih + 1
		if safe(report[:ih] + report[ih+1:]) or safe(report[:ih+1] + report[ih+2:]):
			return True

	return False


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
		elif dampen(report):
			dampsafe += 1
		elif trial_dampen(report):
			print("Uh oh:", report)

	print(numsafe)
	print(numsafe + dampsafe)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)