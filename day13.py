#!/usr/local/bin/python3
dInput = {}
def get_position(iLength, iTime, iDelay = 0):
	iTimeNew = iTime + iDelay
	iLoop = iTimeNew // (iLength - 1)
	iPos = 0
	if iLoop % 2 == 0:
		iPos = iTimeNew % (iLength - 1)
	else:
		iPos = (iLength - 1) - (iTimeNew % (iLength - 1))
	return iPos

def q_1():
	global dInput
	r = 0
	for key, value in dInput.items():
		if get_position(int(value), int(key)) == 0:
			r += int(value) * int(key)
	return r

def q_2():
	global dInput
	iDelay = 0
	bCatched = False
	while True:
		bCatched = False
		for key, value in dInput.items():
			if get_position(int(value), int(key), iDelay) == 0:
				bCatched = True
				break;
		if bCatched:
			iDelay += 1
		else:
			return iDelay


def main():
	with open('input.txt') as f:
		for content in f:
			content = content.rstrip('\n')
			iDepth, iRange = content.split(': ')
			dInput[iDepth] = iRange
	print(q_1())
	print(q_2())

# end of main

if __name__ == '__main__':
	main()