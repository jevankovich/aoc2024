#!/usr/bin/python3
import importlib
import time

def main():
	for day in range(1, 26):
		name = "day" + str(day)
		try:
			module = importlib.import_module(name)
			with open(f"{name}.txt", 'r') as f:
				lines = f.readlines()

			print(name)
			start_time = time.perf_counter()
			module.main(lines)
			end_time = time.perf_counter()
			print(f"{end_time - start_time:.3g} seconds")
			print()

		except ModuleNotFoundError:
			pass
		except FileNotFoundError:
			pass

if __name__ == '__main__':
	main()
