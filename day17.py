#!/usr/local/bin/python3
class spinLock():
    def __init__(self, stepLength):
        self.listSpinLock = [0]
        self.stepLength = stepLength
        self.currentPosition = 0

    def getMovedPosition(self, n, listLength=None):
        if listLength is None:
            listLength = len(self.listSpinLock)
        self.currentPosition = (self.currentPosition + self.stepLength) \
            % listLength + 1

    def insertNewValue(self, n):
        self.listSpinLock = self.listSpinLock[:self.currentPosition] + [n] \
            + self.listSpinLock[self.currentPosition:]

    def move(self, n):
        self.getMovedPosition(n)
        self.insertNewValue(n)


class fastSpinLock(spinLock):
    def __init__(self, stepLength):
        spinLock.__init__(self, stepLength)
        self.zeroPosition = 0
        self.listLength = 1
        self.afterZero = None

    def fastMove(self, n):
        self.getMovedPosition(n, self.listLength)
        if self.currentPosition == 1:
            self.afterZero = n
        self.listLength += 1


def q_1():
    o_1 = spinLock(394)
    for i in range(1, 2018):
        o_1.move(i)
        # print(o_1.list, o_1.currentPosition)
    return o_1.listSpinLock[o_1.listSpinLock.index(2017) + 1]


def q_2():
    o_2 = fastSpinLock(394)
    for i in range(1, 50000000):
        o_2.fastMove(i)
        # print(o_1.list, o_1.currentPosition)
    return o_2.afterZero


def main():
    print(q_1())
    print(q_2())
# end of main


if __name__ == '__main__':
    main()
