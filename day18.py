#!/usr/local/bin/python3
class playSounds():
    def __init__(self):
        self.d = {}
        self.playSounds = []

    def getValue(self, s):
        try:
            return int(s)
        except ValueError:
            if s not in self.d:
                self.d[s] = 0
            return self.d[s]

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
    return ps.playSounds


def main():
    print(q_1())
# end of main


if __name__ == '__main__':
    main()
