#!/usr/local/bin/python3
def FindEvenlyDivisibleValues(l):
	while len(l) > 0:
		x = l.pop(0)
		for y in l:
			if x % y == 0 or y % x == 0:
				return max(x, y), min(x, y)

def main():
	arr = []
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			arr.append(list(map(int, content.split('\t'))))
	#s = '91212129'
	r, r2 = 0, 0
	for i in range(len(arr)):
		r += max(arr[i]) - min(arr[i])
		x, y = FindEvenlyDivisibleValues(arr[i])
		r2 += x / y
	print(r, r2)

# end of main

if __name__ == '__main__':
	main()

