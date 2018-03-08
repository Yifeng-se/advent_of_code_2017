#!/usr/local/bin/python3
l = []
dInput = {}

def findConnectedNodes(d, k):
	global l
	if k in l:
		pass
	else:
		l += [k]
		if k in d:
			for x in d[k]:
				findConnectedNodes(d, x)
	return

def q_1():
	global dInput, l
	findConnectedNodes(dInput, 0)
	print(len(l))

def q_2():
	ll = []
	global l, dInput
	foundInLL = False
	for k in dInput:
		foundInLL = False
		for x in ll:
			if k in x:
				foundInLL = True
				continue
		if not foundInLL:
			l = []
			findConnectedNodes(dInput, k)
			ll.append(l[:])
	print(len(ll))

def main():
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			note, s_connect = content.split(' <-> ')
			dInput[int(note)] = list(map(int, s_connect.split(',')))
	q_1()
	q_2()

# end of main

if __name__ == '__main__':
	main()