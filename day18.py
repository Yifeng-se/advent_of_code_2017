#!/usr/local/bin/python3
class storeValues():
    def __init__(self, pID=0):
        self.d = {}
        self.pID = pID
        self.d['p'] = pID

    def getValue(self, s):
        try:
            return int(s)
        except ValueError:
            if s not in self.d:
                self.d[s] = 0
            return self.d[s]


class playSounds(storeValues):
    def __init__(self):
        storeValues.__init__(self)
        self.playSounds = []

    def getInstruction(self, s):
        cmds = s.split(' ')
        if cmds[0] == 'snd':
            self.playSounds.append(self.getValue(cmds[1]))
            return 1
        elif cmds[0] == 'set':
            self.d[cmds[1]] = self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'add':
            if cmds[1] not in self.d:
                self.d[cmds[1]] = 0
            self.d[cmds[1]] += self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'mul':
            if cmds[1] not in self.d:
                self.d[cmds[1]] = 0
            self.d[cmds[1]] *= self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'mod':
            if cmds[1] not in self.d:
                self.d[cmds[1]] = 0
            self.d[cmds[1]] %= self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'rcv':
            if self.getValue(cmds[1]) > 0:
                self.playSounds.append(self.playSounds[-1])
            return 1
        elif cmds[0] == 'jgz':
            if self.getValue(cmds[1]) > 0:
                return self.getValue(cmds[2])
            else:
                return 1


class sendReceives(storeValues):
    def __init__(self, pID):
        storeValues.__init__(self, pID)
        self.recevie = []
        self.send = []
        self.currentStep = ''

    def getInstruction(self, s):
        cmds = s.split(' ')
        self.currentStep = cmds[0]
        if cmds[0] == 'snd':
            self.send.append(self.getValue(cmds[1]))
            return 1
        elif cmds[0] == 'set':
            self.d[cmds[1]] = self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'add':
            if cmds[1] not in self.d:
                self.d[cmds[1]] = 0
            self.d[cmds[1]] += self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'mul':
            if cmds[1] not in self.d:
                self.d[cmds[1]] = 0
            self.d[cmds[1]] *= self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'mod':
            if cmds[1] not in self.d:
                self.d[cmds[1]] = 0
            self.d[cmds[1]] %= self.getValue(cmds[2])
            return 1
        elif cmds[0] == 'rcv':
            if len(self.recevie) > 0:
                self.d[cmds[1]] = self.recevie.pop(0)
                return 1
            else:
                return 0
        elif cmds[0] == 'jgz':
            if self.getValue(cmds[1]) > 0:
                return self.getValue(cmds[2])
            else:
                return 1


def q_1():
    ps = playSounds()
    steps, i = [], 0
    with open('inputs/input18.txt') as f:
        for content in f:
            content = content.rstrip('\n')
            steps.append(content)

    while True:
        if steps[i][:3] == 'rcv':
            break
        else:
            i += ps.getInstruction(steps[i])
    return ps.playSounds[-1]


def q_2():
    sr0 = sendReceives(0)
    sr1 = sendReceives(1)
    steps, i0, i1, m0, m1 = [], 0, 0, 0, 0
    with open('inputs/input18.txt') as f:
        for content in f:
            content = content.rstrip('\n')
            steps.append(content)

    while True:
        m0 = sr0.getInstruction(steps[i0])
        if sr0.currentStep == 'snd':
            sr1.recevie.append(sr0.send[-1])
        m1 = sr1.getInstruction(steps[i1])
        if sr1.currentStep == 'snd':
            sr0.recevie.append(sr1.send[-1])
        if (sr1.recevie == [] and sr0.recevie == [] and
                sr1.currentStep == 'rcv' and sr0.currentStep == 'rcv'):
            break

        i0 += m0
        i1 += m1
    return len(sr1.send)


def main():
    print(q_1())
    print(q_2())
# end of main


if __name__ == '__main__':
    main()
