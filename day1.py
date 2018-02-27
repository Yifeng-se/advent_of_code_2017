#!/usr/local/bin/python3
def findTheSum(s, skipCnt):
	s += s[:skipCnt]
	l = list(s)
	r = 0
	while len(l) > skipCnt:
		if l.pop(0) == l[skipCnt - 1]:
			r += int(l[skipCnt - 1])
	return r

def main():
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
	s = content
	ans_1 = findTheSum(s, 1)
	ans_2 = findTheSum(s, int(len(s)/2))
	print(ans_1, ans_2)

# end of main

if __name__ == '__main__':
	main()
