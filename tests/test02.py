#!/usr/local/bin/python3
import sys
sys.path.insert(0, '../')

import day02

def test_1(x, y):
	assert day02.q_1(x) == y

def test_2(x, y):
	assert day02.q_2(x) == y

test_1([5,1,9,5], 8)
test_1([7,5,3], 4)
test_1([2,4,6,8], 6)

test_2([5, 9, 2, 8], 4)
test_2([9, 4, 7, 3], 3)
test_2([3, 8, 6, 5], 2)