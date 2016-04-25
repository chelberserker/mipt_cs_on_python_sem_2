from pygame.locals import *
from math import floor
import os
import time

def recalculate(field):
    for i in range(1, len(field)):
        for j in range(1, len(field)):
            num = 0
            for k in range(-1, 1):
                for t in range(-1, 1):
                    if field[i+k][j+t] == 1:
                        num += 1
            if num == 3:
                if field[i,j] == 0:
                    field[i,j] = 1
                else:
                    pass
            if num == 2:
                pass
            if num > 3:
                if field[i,j] == 1:
                    field[i,j] = 0
                else:
                    pass

def init_field(filename):
    input = open(filename, 'r')
    N = 25
    field = []
    field.append(['*' for i in range(N+2)])
    for i in range(1, N+1):
        str = input.readline()
        field.append(['*'])
        for j in range(1, N+1):
            field[i].append(str[j-1])
        field[i].append('*')
    field.append(['*' for i in range(N+2)])
    return field

if __name__ == '__main__':
    field = init_field('input.txt')
    recalculate(field)
    for i in range(len(field)):
        print(field[i])

    while 1:
        recalculate(field)
        time.sleep(5)
        print(field)










