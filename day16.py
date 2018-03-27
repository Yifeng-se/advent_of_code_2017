#!/usr/local/bin/python3
class dancePrograms():
    def __init__(self, c):
        self.lPrograms = []
        for x in range(ord('a'), ord(c) + 1):
            self.lPrograms.append(chr(x))

    def danceS(self, n):
        self.lPrograms = self.lPrograms[-n:] + self.lPrograms[:-n]

    def danceX(self, x, y):
        if x > y:
            x, y = y, x
        self.lPrograms = self.lPrograms[:x] + [self.lPrograms[y]] \
            + self.lPrograms[x + 1:y] + [self.lPrograms[x]] \
            + self.lPrograms[y + 1:]

    def danceP(self, x, y):
        self.danceX(self.lPrograms.index(x),
                    self.lPrograms.index(y))

    def danceCmdStr(self, s):
        if s[0] == 's':
            self.danceS(int(s[1:]))
        elif s[0] == 'x':
            lTmp = s[1:].split('/')
            self.danceX(int(lTmp[0]), int(lTmp[1]))
        elif s[0] == 'p':
            lTmp = s[1:].split('/')
            self.danceP(lTmp[0], lTmp[1])


def q_1():
    o_1 = dancePrograms('p')
    steps = []
    with open('inputs/input16.txt') as f:
        for content in f:
            content = content.rstrip('\n')
        steps = content.split(',')
        for x in steps:
            o_1.danceCmdStr(x)
    return ''.join(o_1.lPrograms)


def q_2():
    o_2 = dancePrograms('p')
    l2 = o_2.lPrograms[:]
    steps = []
    iRepeat = 0
    cache = []
    with open('inputs/input16.txt') as f:
        for content in f:
            content = content.rstrip('\n')
        steps = content.split(',')
        for i in range(1000000000):
            for x in steps:
                o_2.danceCmdStr(x)
            if o_2.lPrograms == l2:
                iRepeat = i + 1
                break
            else:
                cache.append(o_2.lPrograms)

        return ''.join(cache[1000000000 % iRepeat - 1])


def main():
    print(q_1())
    print(q_2())
# end of main


if __name__ == '__main__':
    main()
