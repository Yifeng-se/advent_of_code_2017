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

def q_1():
	obj_q1 = KnotHash(256)
	#obj_test = KnotHash(5)
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			inputList = list(map(int, content.split(',')))
			for i in inputList:
				obj_q1.modifyList(i)
			print(obj_q1.list)

def q_2():
	obj_q2 = KnotHash(256)
	inputList, denseHash = [], []
	#obj_test = KnotHash(5)
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			for x in content:
				inputList.append(ord(x))
			inputList += [17, 31, 73, 47, 23]
			for i in range(64):
				for m in inputList:
					obj_q2.modifyList(m)
			for l in [obj_q2.list[i:i + 16] for i in range(0, len(obj_q2.list), 16)]:
				denseHash.append(0)
				for x in l:
					denseHash[-1] = denseHash[-1] ^ x
			for i in range(len(denseHash)):
				denseHash[i] = format(denseHash[i], 'x')
			print(''.join(denseHash))

def main():
	q_2()

# end of main

if __name__ == '__main__':
	main()