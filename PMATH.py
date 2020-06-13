from math import sqrt as _s

def factorial(x):
 t=x
 for i in range(x-1,0,-1):t*=i
 return t

def isclose(a,b,rel_tol=1e-09,abs_tol=0.0):
 return abs(a-b)<=max(rel_tol*max(abs(a),abs(b)),abs_tol)

def hypot(x,y):return _s(x*x+y*y)

def copy_negate(x):return -x
