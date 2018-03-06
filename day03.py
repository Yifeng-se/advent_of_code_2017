#!/usr/local/bin/python3
def q_1(n):
	"""
	Return Manhattan Distance between the location of the data and square 1
	17  16  15  14  13
	18   5   4   3  12
	19   6   1   2  11
	20   7   8   9  10
	21  22  23---> ...
	"""
	# Basically it is a growing length square, by calculate the length, we can find the position
	# Also we can get the direction of this number
	lDirection = ['r', 'u', 'l', 'd']
	iLength = 0
	r = 0
	total = 1
	token = 0
	iTurn = -1
	while total < n:
		iLength += 1
		token = 1
		total += iLength
		iTurn += 1
		if total < n:
			total += iLength
			token = 0
			iTurn += 1

	return ((iTurn - 1) // 4 + 1) + abs((iLength + 1) // 2 - (total - n)), lDirection[iTurn % 4]

def get_sum_around(l, i, j):
	"""
	for a given 2d array l[i][j], look around point x,y, and get all 8 other number's sum
	"""
	iSum = 0
	if i == 0 and j == 0 and len(l) == 1:
		return 1

	if i > 0:
		if j > 0:
			iSum += l[i - 1][j - 1]
		iSum += l[i - 1][j]
		if j < len(l[i]) - 1:
			iSum += l[i - 1][j + 1]

	if j > 0:
		iSum += l[i][j - 1]
	iSum += l[i][j]
	if j < len(l[i]) - 1:
		iSum += l[i][j + 1]

	if i < len(l) - 1:
		if j > 0:
			iSum += l[i + 1][j - 1]
		iSum += l[i + 1][j]
		if j < len(l[i]) - 1:
			iSum += l[i + 1][j + 1]
	return iSum

def q_2(n):
	#now we need to build the 2D array first
	l = [[0]]
	r = 0
	iCnt, i, j = 0, -1, 0
	iLast = 0
	while iLast < n:
		iCnt += 1
		#For every new input value, we need to decide its moving direction, we can get it from q_1
		iStep, sDirection = q_1(iCnt)
		#print(iCnt, sDirection, l, i, j)
		#And then get the value for the new input
		#Sometime we need to extend the array, so recalculate value for i, j
		if sDirection == 'r':
			j += 1
			if j > len(l[i]) - 1:
				for x in range(len(l)):
					l[x] = l[x] + [0]
		elif sDirection == 'l':
			j -= 1
			if j < 0:
				for x in range(len(l)):
					l[x] = [0] + l[x]
				j = 0
		elif sDirection == 'u':
			i -= 1
			if i == -1:
				l = [[0] * len(l[0])] + l
				i = 0
		elif sDirection == 'd':
			i += 1
			if i > len(l) - 1:
				l = l + [[0] * len(l[0])]

		iLast = get_sum_around(l, i, j)
		l[i][j] = iLast
	return iLast

def main():
	print(q_1(265149))
	print(q_2(265149))
#	for i in range(1, 30):
#		print(i, q_1(i))
# end of main

if __name__ == '__main__':
	main()

