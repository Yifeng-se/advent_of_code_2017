#!/usr/local/bin/python3
def cleanGarbage(s):
	bInGarbage, passNext = False, False
	r, total_garbage = '', ''
	for x in s:
		if bInGarbage:
			if passNext:
				passNext = False
				continue
			if x == '!':
				passNext = True
				continue
			else:
				passNext = False
				if x != '>':
					total_garbage += x
			if x == '>':
				bInGarbage = False
				continue
			continue
		else:
			if x == '<':
				bInGarbage = True
				continue
			else:
				r += x
	return r, total_garbage

def getScore(s):
	iCurr, iSum = 1, 0
	for x in s:
		if x == '{':
			iSum += iCurr
			iCurr += 1
		elif x == '}':
			iCurr -= 1
		elif x== ',':
			pass
	return iSum

def q_1():
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			clean_content, total_garbage = cleanGarbage(content)
			print(clean_content, len(total_garbage))
			print(getScore(clean_content))

def main():
	q_1()

# end of main

if __name__ == '__main__':
	main()