#!/usr/local/bin/python3
import sys
sys.path.insert(0, '../')
import day19


def test_1():
    in_puzzle = [
        list('     |          '),
        list('     |  +--+    '),
        list('     A  |  C    '),
        list(' F---|----E|--+ '),
        list('     |  |  |  D '),
        list('     +B-+  +--+ ')]
    pk0 = day19.packet(in_puzzle)
    pk0.moveUntilEnd()
    print('Total steps:' + str(pk0.stepCount))
    print('end', pk0.s)


def main():
    test_1()
# end of main


if __name__ == '__main__':
    main()
