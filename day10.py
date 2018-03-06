#!/usr/local/bin/python3
def modifyList(l, i, iStartPoint, iSkipSize):
	iEndPoint, iNewSkipSize, iOverSize = iStartPoint, iSkipSize + 1, 0
	bTooLong = False
	if iStartPoint + i > len(l):
		iOverSize = iStartPoint + i - len(l)
		l += l
		bTooLong = True
	l_tmp = l[iStartPoint: iStartPoint + i][::-1]
	for j in range(iStartPoint, iStartPoint + i):
		l[j] = l_tmp[j - iStartPoint]
	iEndPoint += i + iSkipSize
	iSkipSize += 1
	if bTooLong:
		iEndPoint = iEndPoint % (len(l) / 2)
		l = l[len(l) // 2 : len(l) // 2 + iOverSize] + l[iOverSize: len(l) // 2]

	return l, int(iEndPoint % len(l)), iNewSkipSize
def q_1():
	resultList = list(range(256))
	iStartPoint, iSkipSize = 0, 0
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			inputList = list(map(int, content.split(',')))
			for i in inputList:
				resultList, iStartPoint, iSkipSize = modifyList(resultList, i, iStartPoint, iSkipSize)
				print(resultList, iStartPoint, iSkipSize)
def main():
	q_1()

# end of main

if __name__ == '__main__':
	main()