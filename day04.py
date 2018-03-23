#!/usr/local/bin/python3
def q_1(ss):
	r = []
	for s in ss:
		s1 = s.split(' ')
		if len(s1) == len(set(s1)):
			r.append(s1)
	print(len(r))
	return r

def q_2(ss):
	r = []
	for s in ss:
		d = {}
		s1 = s.split(' ') #i.e. ['a', 'ab', 'abc', 'abd', 'abf', 'abj']
		for i in range(len(s1)):
			s1[i] = ''.join(sorted(s1[i]))
		if len(s1) == len(set(s1)):
			r.append(s1)
	print(len(r))
	return r

def main():
	ss = []
	with open('inputs/input04.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			ss.append(content)
	q_1(ss)
	q_2(ss)

# end of main

if __name__ == '__main__':
	main()