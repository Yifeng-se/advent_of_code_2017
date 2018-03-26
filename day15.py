#!/usr/local/bin/python3
def q_1():
    FactorA = 16807
    FactorB = 48271
    ModValue = 2147483647
    StartValueA = 873  # 65
    StartValueB = 583  # 8921
    PairNA, PairNB = StartValueA, StartValueB
    iCnt = 0
    for i in range(40000000):
        PairNA = (PairNA * FactorA) % ModValue
        PairNB = (PairNB * FactorB) % ModValue
        # print(bin(PairNA)[2:].zfill(32), bin(PairNB)[2:].zfill(32))
        if bin(PairNA)[-16:] == bin(PairNB)[-16:]:
            iCnt += 1
    return iCnt


def q_2():
    FactorA = 16807
    FactorB = 48271
    ModValue = 2147483647
    StartValueA = 873  # 65
    StartValueB = 583  # 8921
    PairNA, PairNB = StartValueA, StartValueB
    iCnt = 0

    def getNextA(a):
        while True:
            a = (a * FactorA) % ModValue
            if (a % 4 == 0):
                return a

    def getNextB(b):
        while True:
            b = (b * FactorB) % ModValue
            if (b % 8 == 0):
                return b

    for i in range(5000000):
        PairNA = getNextA(PairNA)
        PairNB = getNextB(PairNB)
        # print(bin(PairNA)[2:].zfill(32), bin(PairNB)[2:].zfill(32))
        if bin(PairNA)[-16:] == bin(PairNB)[-16:]:
            iCnt += 1
    return iCnt


def main():
    print(q_1())
    print(q_2())

# end of main


if __name__ == '__main__':
    main()
