#!/usr/local/bin/python3
def q_1(l):
	return max(l) - min(l)

def q_2(l):
	while len(l) > 0:
		x = l.pop(0)
		for y in l:
			if x % y == 0 or y % x == 0:
				return max(x, y) / min(x, y)

def main():
	arr = []
	with open('inputs/input02.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			arr.append(list(map(int, content.split('\t'))))
	r, r2 = 0, 0
	for i in range(len(arr)):
		r += q_1(arr[i])
		r2 += q_2(arr[i])
	print(r)
	print(r2)

# end of main

if __name__ == '__main__':
	main()

