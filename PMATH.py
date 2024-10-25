from math import sqrt as _s,gcd as g


def comb(n,k):
	if k>n:return 0

	return int(factorial(n) / (factorial(k) * factorial(n - k)))

def copy_negate(x):
	return -x

def factorial(x):
	t=x
	for i in range(x-1,0,-1):
		t*=i
	return t

def gcd(a,b=None):
	if not b:return a
	m = abs(max(a,b))
	n = abs(min(a,b))
	g = 1 

	for i in range(1, m //2 + 1 ):
		if m % i == 0 and n % i == 0:g = i		
	return g

def hypot(x,y):
	return _s(x*x+y*y)

def isclose(a,b,rel_tol=1e-09,abs_tol=0.0):
	return abs(a-b)<=max(rel_tol*max(abs(a),abs(b)),abs_tol)


inf = float("inf")

nan = float("nan")

