#!/usr/local/bin/python3
class packet():
    def __init__(self, diagram=[[]]):
        self.diagram = diagram
        self.s = ''
        self.direction = ''
        self.currPos = [0, 0]
        self.stepCount = 0
        if '|' in diagram[0]:
            self.currPos[1] = diagram[0].index('|')
            self.direction = 'd'

    def move(self, debug=False):
        if self.direction == 'd':
            self.currPos[0] += 1
        elif self.direction == 'u':
            self.currPos[0] -= 1
        elif self.direction == 'l':
            self.currPos[1] -= 1
        elif self.direction == 'r':
            self.currPos[1] += 1
        self.getNewDirection()
        if (self.diagram[self.currPos[0]][self.currPos[1]] not in
                [' ', '+', '-', '|']):
            self.s += self.diagram[self.currPos[0]][self.currPos[1]]
        if debug:
            print(self.currPos, self.direction, self.s)
        self.stepCount += 1

    def checkEnd(self):
        if (self.currPos[0] < 0 or
                self.currPos[1] < 0 or
                self.currPos[0] > len(self.diagram) or
                self.currPos[1] > len(self.diagram[self.currPos[0]]) or
                self.diagram[self.currPos[0]][self.currPos[1]] == ' '):
            return True
        else:
            return False

    def getNewDirection(self):
        if self.diagram[self.currPos[0]][self.currPos[1]] != '+':
            return
        else:
            if (self.currPos[1] + 1 < len(self.diagram[self.currPos[0]]) and
                    self.direction != 'l' and
                    self.diagram[self.currPos[0]][self.currPos[1] + 1] not in
                    [' ', '|']):
                self.direction = 'r'
            elif (self.currPos[1] - 1 >= 0 and
                    self.direction != 'r' and
                    self.diagram[self.currPos[0]][self.currPos[1] - 1] not in
                    [' ', '|']):
                self.direction = 'l'
            elif (self.currPos[0] + 1 < len(self.diagram) and
                    self.currPos[1] < len(self.diagram[self.currPos[0] + 1]) and
                    self.direction != 'u' and
                    self.diagram[self.currPos[0] + 1][self.currPos[1]] not in
                    [' ', '-']):
                self.direction = 'd'
            elif (self.currPos[0] - 1 >= 0 and
                    self.currPos[1] < len(self.diagram[self.currPos[0] - 1]) and
                    self.direction != 'd' and
                    self.diagram[self.currPos[0] - 1][self.currPos[1]] not in
                    [' ', '-']):
                self.direction = 'u'
            else:
                self.direction = ''

    def moveUntilEnd(self):
        while not self.checkEnd():
            self.move()


def q_1():
    l_input = []
    with open('inputs/input19.txt') as f:
        for content in f:
            content = content.rstrip('\n')
            l_input.append(list(content))
    pk1 = packet(l_input)
    pk1.moveUntilEnd()
    print('Total steps: ' + str(pk1.stepCount))
    print('Ending: ', pk1.currPos)
    return(pk1.s)


def main():
    print(q_1())
# end of main


if __name__ == '__main__':
    main()
