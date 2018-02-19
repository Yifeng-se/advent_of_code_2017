#!/usr/local/bin/python3
def main():
	i = 0
	r = 0
	n = 265149
	total = 1
	first = 0
	while total < n:
		i += 1
		first = 0
		total += i
		if total < n:
			total += i
			first = 1
	print(i, total - n, (first+ i) // 2, + (i+1)//2 - (total - n))

	return r

# end of main

if __name__ == '__main__':
	main()

