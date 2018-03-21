#!/usr/local/bin/python3
class KnotHash():
	def __init__(self, size):
		self.list = list(range(size))
		self.iSkipSize = 0
		self.iCurrentPoint = 0
		self.size = size

	def modifyList(self, iLength):
		iEndPoint, iOverSize = self.iCurrentPoint, 0
		bTooLong = False
		if self.iCurrentPoint + iLength > self.size:
			iOverSize = self.iCurrentPoint + iLength - self.size
			self.list += self.list
			bTooLong = True
		l_tmp = self.list[self.iCurrentPoint: self.iCurrentPoint + iLength][::-1]
		for j in range(self.iCurrentPoint, self.iCurrentPoint + iLength):
			self.list[j] = l_tmp[j - self.iCurrentPoint]
		if bTooLong:
			self.list = self.list[self.size : self.size + iOverSize] + self.list[iOverSize: self.size]
		self.iCurrentPoint = (self.iCurrentPoint + iLength + self.iSkipSize) % self.size
		self.iSkipSize += 1

def set_block_to_zero(l, x, y):
	l[x][y] = 0
	if x > 0 and l[x-1][y] == 1:
		set_block_to_zero(l, x-1, y)
	if x < len(l[0]) - 1 and l[x+1][y] == 1:
		set_block_to_zero(l, x+1, y)
	if y > 0 and l[x][y-1] == 1:
		set_block_to_zero(l, x, y-1)
	if y < len(l) - 1 and l[x][y+1] == 1:
		set_block_to_zero(l, x, y+1)


def q_1():

	inputList, denseHash, salt = [], [], [17, 31, 73, 47, 23]
	slices = 16
	iSum = 0
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			for i in range(128):
				obj_q1 = KnotHash(256)
				inputList, denseHash, sBin = [], [], ''
				content_i = content + '-' + str(i)
				for x in content_i:
					inputList.append(ord(x))
				inputList += salt
				for i in range(64):
					for m in inputList:
						obj_q1.modifyList(m)
				for l in [obj_q1.list[i:i + slices] for i in range(0, len(obj_q1.list), slices)]:
					denseHash.append(0)
					for x in l:
						denseHash[-1] = denseHash[-1] ^ x
				for i in range(len(denseHash)):
					denseHash[i] = format(denseHash[i], 'x').rjust(2, '0')
				for i in ''.join(denseHash):
					sBin += bin(int(i, 16))[2:].rjust(4, '0')
				for i in sBin:
					iSum += int(i)
			print(iSum)

def q_2():
	inputList, denseHash, salt = [], [], [17, 31, 73, 47, 23]
	slices = 16
	iSum, iCntBlock = 0, 0
	diskArr = []
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			for i in range(128):
				obj_q1 = KnotHash(256)
				inputList, denseHash, sBin = [], [], ''
				content_i = content + '-' + str(i)
				for x in content_i:
					inputList.append(ord(x))
				inputList += salt
				for i in range(64):
					for m in inputList:
						obj_q1.modifyList(m)
				for l in [obj_q1.list[i:i + slices] for i in range(0, len(obj_q1.list), slices)]:
					denseHash.append(0)
					for x in l:
						denseHash[-1] = denseHash[-1] ^ x
				for i in range(len(denseHash)):
					denseHash[i] = format(denseHash[i], 'x').rjust(2, '0')
				for i in ''.join(denseHash):
					sBin += bin(int(i, 16))[2:].rjust(4, '0')
				diskArr.append(list(map(int, sBin)))

			for i in range(len(diskArr[0])):
				for j in range(len(diskArr)):
					if diskArr[i][j] == 1:
						set_block_to_zero(diskArr, i, j)
						iCntBlock += 1
			print(iCntBlock)

def main():
	#q_1()
	q_2()

# end of main

if __name__ == '__main__':
	main()