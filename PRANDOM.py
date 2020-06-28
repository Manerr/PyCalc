from random import randint as _r
def choice(seq):return seq[_r(0,len(seq)-1)]

def sample(population,k):
 population=list(population)
 t=[]
 s=0
 for i in range(k):
  s=_r(0,len(population)-1)
  t+=[population[s]]
  del population[s]
 return t

def shuffle(x,r=0):
 return sample(x,len(x))
