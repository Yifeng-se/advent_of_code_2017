#!/usr/local/bin/python3
import math

# The tricky part is to use some set of array to define the position
# since it is a hex grid, I increase the N and S to length 2, so it
# can be present as a 2D array, then devide the Y axis by 2 at the end:
#	move = {
#		'nw': (-1, 1),
#		'n' : (0, 2),
#		'ne': (1, 1),
#		'sw': (-1, -1),
#		'se': (1, -1),
#		's' : (0, -2)
#	}
#
#
#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

class HexGrid():
	container = {
		'nw': (-1, 1),
		'n' : (0, 2),
		'ne': (1, 1),
		'sw': (-1, -1),
		'se': (1, -1),
		's' : (0, -2)
	}

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, s):
		x, y = self.container[s]
		self.x += x
		self.y += y

	def reset(self):
		self.x = 0
		self.y = 0

	def getDistance(self):
		return max(abs(self.x), math.ceil(abs(self.y) / 2))

def q_1():
	obj_q1 = HexGrid(0, 0)
	inputList = []
	iFurthest = 0
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			inputList = content.split(',')
			for i in inputList:
				obj_q1.move(i)
				iFurthest = max(iFurthest, obj_q1.getDistance())
			print('Final distance: ', obj_q1.getDistance(), 'Furthest distance: ', iFurthest)
			obj_q1.reset()

def main():
	q_1()

# end of main

if __name__ == '__main__':
	main()