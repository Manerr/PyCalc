from random import randint as _r,random as _ra

def choice(seq):
    return seq[_r(0,len(seq)-1)]

def sample(population,k):
    population = list(population)
    t = []
    i = 0
    while i < k:
        s = _r(0,len(population) - 1)
        t.append( population[s] )
        del population[s]
        i += 1
    return t


def shuffle(x,r=_ra):
    l = len(x)
    tmp = sample(x,l)
    for i in range(l):
        x[i] = tmp[i]

def randbytes(n):
    return bytes( [_r(0,255) for _ in range(n) ] )


