#!/usr/local/bin/python3
import sys
sys.path.insert(0, '../')

import day03

def test_1(x, y):
	assert day03.q_1(x)[0] == y

def test_2(x, y):
	assert day03.q_2(x) == y

test_1(1, 0)
test_1(12, 3)
test_1(23, 2)
test_1(1024, 31)

