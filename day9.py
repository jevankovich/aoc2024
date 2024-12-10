#!/usr/bin/python3
import sys
import bisect

def partone(line: str) -> int:
	seek = 0
	disk = []
	free = []
	for i, c in enumerate(line):
		blocks = int(c)
		if i % 2 == 0:
			# file block
			for _ in range(blocks):
				disk.append((seek, i // 2))
				seek += 1
		else:
			for _ in range(blocks):
				free.append(seek)
				seek += 1

	compacted = []
	for new in free:
		old, block = disk[-1]
		if new >= old:
			break

		compacted.append((new, block))
		disk.pop()

	checksum = 0
	disk = disk + compacted
	for pos, block in disk:
		checksum += pos * block

	return checksum

def parttwo(line: str) -> int:
	seek = 0

	files = []
	frees = []

	for i in range(0, len(line), 2):
		file_blocks = int(line[i])
		try:
			free_blocks = int(line[i + 1])
		except IndexError:
			free_blocks = 0

		files.append((seek, file_blocks))
		if free_blocks:
			frees.append((seek + file_blocks, free_blocks, i // 2))

		seek += file_blocks + free_blocks
		pass

	for fileid in range(len(files) - 1, 0, -1):
		file = files[fileid]
		pred = files[fileid - 1]

		# find the first free this can fit in
		i = 0
		free = frees[0]
		for i, free in enumerate(frees):
			if free[1] >= file[1]:
				# found it!
				break

		if free[1] < file[1]:
			continue

		if free[0] > file[0]:
			continue

		newpred = files[free[2]]

		# move the file: change its position, shrink the free block we're moving it into
		files[fileid] = (free[0], file[1])
		frees[i] = (free[0] + file[1], free[1] - file[1], fileid)
		# don't bother touching the free block we're moving out of, it doesn't matter

	checksum = 0

	for fileid, file in enumerate(files):
		for i in range(file[1]):
			checksum += fileid * (file[0] + i)

	return checksum


def main(lines: list[str]):
	line = lines[0].strip()

	print(partone(line))
	print(parttwo(line))

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

	main(lines)