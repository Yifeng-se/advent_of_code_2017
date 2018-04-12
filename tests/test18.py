#!/usr/local/bin/python3
import sys
sys.path.insert(0, '../')
import day18


def test_2():
    sr0 = day18.sendReceives(0)
    sr1 = day18.sendReceives(1)
    steps, i0, i1 = [], 0, 0
    steps = [
        'snd 1',
        'snd 2',
        'snd p',
        'rcv a',
        'rcv b',
        'rcv c',
        'rcv d']
    while True:
        i0 += sr0.getInstruction(steps[i0])
        if sr0.currentStep == 'snd':
            sr1.recevie.append(sr0.send[-1])
        i1 += sr1.getInstruction(steps[i1])
        if sr1.currentStep == 'snd':
            sr0.recevie.append(sr1.send[-1])
        if (sr1.recevie == [] and sr0.recevie == [] and
                sr1.currentStep == 'rcv' and sr0.currentStep == 'rcv'):
            break

    print('end', sr1.send)


def main():
    test_2()
# end of main


if __name__ == '__main__':
    main()
