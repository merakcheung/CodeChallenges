'''
given a 6-sided dice, play the well known game of rolling dice for n times.
what is the expected return
'''
from math import floor

def solution(n):
    if n ==0:
        return 0
    elif n == 1:
        return 3
    prevret = 3.0
    count = 2
    fmap = {2: 10.0/3, 3: 3.0, 4: 2.5, 5: 11.0/6, 6: 1.0 }


    while (count <n):
        f = floor(prevret)
        sp = f/6.0 * prevret
        sp += fmap[f+1]
        prevret = sp
        count += 1

    return prevret

if __name__ == '__main__':
    for i in range(100,1000,100):
        print solution(i)