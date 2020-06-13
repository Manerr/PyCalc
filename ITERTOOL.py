def accumulate(iterable,func=None):
 tot=next(iter(iterable))
 if not func:tot=0
 yield tot
 for i in iterable:
  if not func:tot+=i
  else:tot=func(tot,i)
  yield tot

def count(start,step=1):
 x=0
 while 1:
  yield start+x*step
  x+=1

def cycle(p):
 while 1:
  for i in p:
   yield i

def repeat(elem,n=-1):
 i=0
 while i<n:
  yield elem
  if n!=-1:i+=1

def chain(*iterables):
 for i in iterables:
  for j in i:yield j

def compress(data,selector):
 return [data[i] for i in range(len(data)) if selector[i]]

def filterfalse(func,iterable):
 if func is None:
  func=bool
 for i in iterable:
  if not func(i):yield i

def islice(iterable,start,stop=False,step=1):
 if stop==None:stop=len(iterable)
 if not stop:start,stop=0,start
 for i in range(start,stop,step):
  yield iterable[i]

def starmap(func,i):
 for args in i:yield func(*args)
def takewhile(func,i):
 for j in i:
  if func(j):yield j
  else:break
