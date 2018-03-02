#!/usr/local/bin/python3
import re

def q_1():
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
			return _v

class Disc(object):
	"""docstring for Disc"""
	def __init__(self, name, weight):
		super(Disc, self).__init__()
		self.name = name
		self.weight = weight
		self.children = []
		self.level = 0
	def add(self, child):
		self.children.append(child)
		child.moveDown(self.level + 1)
	def getTotalWeight(self):
		r = 0
		for x in self.children:
			r += x.getTotalWeight()
		r += self.weight
		return r
	def ChildrenWeightDiff(self):
		r = False
		for x in self.children:
			if self.children[0].getTotalWeight() != x.getTotalWeight():
				r = True
				break
		return r
	def moveDown(self, n):
		self.level += n
		for x in self.children:
			x.moveDown(n)
def q_2():
	l = []
	d = {}
	parentname, weight, children = '', 0, []
	i = 0
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			parentname, weight = content[:content.index('(') - 1], int(content[content.index('(') + 1:content.index(')')])
			if parentname in d:
				l[d[parentname]].weight = weight
			else:
				l.append(Disc(parentname, weight))
				d[parentname] = i
				i += 1
			if '->' in content:
				children = content[content.index('-> ') + 3:].split(', ')
				for x in children:
					if x in d:
						pass
					else:
						l.append(Disc(x, 0))
						d[x] = i
						i += 1
					l[d[parentname]].add(l[d[x]])

	maxDiffWeightLevel = 0
	maxDiffWeightName = ''
	for x in l:
		if x.ChildrenWeightDiff():
			if maxDiffWeightLevel < x.level:
				maxDiffWeightName = x.name
				maxDiffWeightLevel = x.level
	d2 = {}
	for x in l[d[maxDiffWeightName]].children:
		if x.getTotalWeight() in d2:
			d2[x.getTotalWeight()] += [x.name]
		else:
			d2[x.getTotalWeight()] = [x.name]
	wrong_name, wrong_weight, right_weight = 0, '', 0
	for k, x in d2.items():
		if len(x) == 1:
			wrong_name = x[0]
			wrong_weight = k
		else:
			right_weight = k
	print(l[d[wrong_name]].weight - (wrong_weight - right_weight))

	return 0

def main():
	q_2()

# end of main

if __name__ == '__main__':
	main()