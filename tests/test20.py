#!/usr/local/bin/python3
import sys
sys.path.insert(0, '../')
import day20


def test_1():
    in_puzzle = [
        'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
        'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
        'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
        'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']
    l_particle, iParticle = [], 0
    for content in in_puzzle:
            # p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>
            lTmp = content.split(', ')
            p = lTmp[0][3:-1].split(',')
            v = lTmp[1][3:-1].split(',')
            a = lTmp[2][3:-1].split(',')
            l_particle.append(day20.particle(iParticle, p, v, a))

    oldMinDistance, minDistance = None, None
    while oldMinDistance is None or oldMinDistance > minDistance:
        print(oldMinDistance, minDistance)
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
            l_particle.remove(x)
        oldMinDistance = minDistance
        minDistance = day20.getMinDistance(l_particle)


    print(l_particle[0].number)
    return len(l_particle)


def main():
    test_1()
# end of main


if __name__ == '__main__':
    main()
