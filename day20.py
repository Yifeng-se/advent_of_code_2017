#!/usr/local/bin/python3
import numpy as np


class particle():
    def __init__(self, n, p, v, a):
        self.number = n
        self.position = np.array(list(map(int, p)))
        self.velocity = np.array(list(map(int, v)))
        self.acceleration = np.array(list(map(int, a)))

    def move(self):
        self.velocity += self.acceleration
        self.position += self.velocity

def getDistances(l):
    l_Distances = []
    for i in range(len(l) - 1):
        l_Distances.append([])
        for j in range(i + 1, len(l)):
            d = l[i].position - l[j].position
            # print(i, j, l[i].position, l[j].position, d)
            l_Distances[i].append(abs(d[0]) + abs(d[1]) + abs(d[2]))
    return l_Distances

def q_1():
    l_particle = []
    min_a, iParticle, iMinParticle = None, 0, 0
    with open('inputs/input20.txt') as f:
        for content in f:
            content = content.rstrip('\n')
            # p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>
            lTmp = content.split(', ')
            p = lTmp[0][3:-1].split(',')
            v = lTmp[1][3:-1].split(',')
            a = lTmp[2][3:-1].split(',')

            l_particle.append(particle(iParticle, p, v, a))

            if (min_a is None or
                    abs(int(a[0])) + abs(int(a[1])) + abs(int(a[2])) < min_a):
                min_a = abs(int(a[0])) + abs(int(a[1])) + abs(int(a[2]))
                iMinParticle = iParticle
            iParticle += 1

    return iMinParticle

def LessExists(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if l2[i][j] < l1[i][j]:
                return True
    return False

def q_2():
    l_particle = []
    iParticle = 0
    with open('inputs/input20.txt') as f:
        for content in f:
            content = content.rstrip('\n')
            # p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>
            lTmp = content.split(', ')
            p = lTmp[0][3:-1].split(',')
            v = lTmp[1][3:-1].split(',')
            a = lTmp[2][3:-1].split(',')

            l_particle.append(particle(iParticle, p, v, a))

            iParticle += 1

    distances, oldDistances = None, None
    l_collision = []
    while (oldDistances is None or
            len(l_collision) > 0 or
            LessExists(oldDistances, distances)):
        d = {}
        l_collision = []

        for p in l_particle:
            p.move()
            if tuple(p.position) in d:
                l_collision.append(p)
                if d[tuple(p.position)] not in l_collision:
                    l_collision.append(d[tuple(p.position)])
            else:
                d[tuple(p.position)] = p
        for x in l_collision:
            # print(x.number)
            l_particle.remove(x)
        oldDistances = distances
        distances = getDistances(l_particle)

    return len(l_particle)


def main():
    print(q_1())
    print(q_2())
# end of main


if __name__ == '__main__':
    main()
