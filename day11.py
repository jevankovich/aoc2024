#!/usr/bin/python3
import sys

def memoblink(memo, num, blinks):
	if blinks == 0:
		return 1

	if (num, blinks) in memo:
		return memo[(num, blinks)]

	if num == '':
		result = memoblink(memo, '1', blinks - 1)
	elif len(num) % 2 == 0:
		half = len(num) // 2
		l = num[:half]
		r = num[half:].lstrip('0')
		result = memoblink(memo, l, blinks - 1) + memoblink(memo, r, blinks - 1)
	else:
		mul = str(int(num) * 2024)
		result = memoblink(memo, mul, blinks - 1)

	memo[(num, blinks)] = result
	return result

def main(lines: list[str]):
	line = lines[0]

	nums = []
	for num in line.split():
		num = num.lstrip('0')
		nums.append(num)

	memo = {}
	total = 0
	for num in nums:
		total += memoblink(memo, num, 25)

	print(total)

	total = 0
	for num in nums:
		total += memoblink(memo, num, 75)

	print(total)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)