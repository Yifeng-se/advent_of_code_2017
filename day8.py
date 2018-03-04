#!/usr/local/bin/python3
import re

def check_condition(a, b, c):
	operators = {'>': "__gt__",
				'<': "__lt__",
				'>=': "__ge__",
				'<=': "__le__",
				'==': "__eq__",
				'!=': "__ne__"}
	return getattr(a, operators[b])(c)

def q_1():
	d = {}
	line = []
	iMax = 0
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			line = content.split(' ')
			if line[0] not in d:
				d[line[0]] = 0
			if line[4] not in d:
				d[line[4]] = 0
			if check_condition(d[line[4]], line[5], int(line[6])):
				if line[1] == 'inc':
					d[line[0]] += int(line[2])
				elif line[1] == 'dec':
					d[line[0]] -= int(line[2])
				if d[line[0]] > iMax:
					iMax = d[line[0]]

	return max(d.values()), iMax

def main():
	print(q_1())

# end of main

if __name__ == '__main__':
	main()