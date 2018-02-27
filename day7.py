#!/usr/local/bin/python3
import re

def main():
	d = {}
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			if '->' not in content:
				pass
			else:
				_key, _value = content.split(' -> ')
				_key = re.sub(' \([0-9]+\)', '', _key)
				_value = _value.split(', ')
				for _one in _value:
					d[_one] = _key
	for _v in d.values():
		if _v not in d:
			print(_v)
			break
	return 0

# end of main

if __name__ == '__main__':
	main()