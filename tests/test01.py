#!/usr/local/bin/python3
import sys
sys.path.insert(0, '../')

import day01

def test_1(x, y):
	assert day01.findTheSum(x, 1) == y

def test_2(x, y):
	assert day01.findTheSum(x, int(len(x)/2)) == y

test_1('1122', 3)
test_1('1111', 4)
test_1('1234', 0)
test_1('91212129', 9)

test_2('1212', 6)
test_2('1221', 0)
test_2('123425', 4)
test_2('123123', 12)
test_2('12131415', 4)
