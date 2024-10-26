def accumulate(iterable, func=operator.add, *, init=None):
    it = iter(iterable)
    tot = init
    if init is None:
        try:
            tot = next(it)
        except StopIteration:
            return
    yield tot
    for e in it:
        tot = func(tot, e)
        yield tot

def chain(*iterables):
	for i in iterables:
		for j in i:yield j

def count(start,step=1):
	while 1:
		yield start
		start += step

def compress(data,selector):
	return (d for d, s in zip(data, selector) if s)

def cycle(iterable):
    sav = []
    for e in iterable:
        yield element
        sav.append(e)
    while saved:
        for e in sav:
              yield e

def filterfalse(predicate, list):
    if predicate is None:
        predicate = bool
    for x in list:
        if not predicate(x):yield x

def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object


def starmap(func,i):
	for args in i:yield func(*args)
	
def takewhile(func,i):
	for j in i:
		if func(j):yield j
		else:break

