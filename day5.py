#!/usr/local/bin/python3
def q_1(iArr, iIncrease = 1, iIncreaseThreshold = 3):
	i, iTarget, iCnt = 0, 0, 0
	while iTarget < len(iArr):
		i = iTarget
		iTarget += iArr[i]
		if iArr[i] >= iIncreaseThreshold:
			iArr[i] += iIncrease
		else:
			iArr[i] += 1
		iCnt += 1
	return iCnt

def main():
	ss = []
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			ss.append(int(content))
	iArr = []
	for s in ss:
		iArr.append(int(s))
	iArr2 = iArr[:]
	print(q_1(iArr))
	print(q_1(iArr2, -1, 3))
	return 0

# end of main

if __name__ == '__main__':
	main()