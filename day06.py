#!/usr/local/bin/python3
def main():
	ss = []
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			ss.append(content)
	iArr = list(map(int, ss[0].split('\t')))
	#iArr = [0, 2, 7 ,0]
	n = len(iArr)
	l = []
	i = 0
	while iArr not in l:
		i += 1
		l.append(iArr[:])
		iMax = max(iArr)
		PosMax = iArr.index(iMax)
		#print(i, iMax, PosMax, iArr)
		iMove = 0
		iArr[PosMax] = 0
		while iMax > 0:
			iMove += 1
			iArr[(PosMax + iMove) % n] += 1
			iMax -= 1
		#print(iArr, l)
	print(i, len(l) - l.index(iArr))
	return 0

# end of main

if __name__ == '__main__':
	main()