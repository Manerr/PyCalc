# COMPARISION


def lt(a,b):return a < b


def le(a,b):return a <= b


def eq(a,b):return a == b


def ne(a,b):return a != b


def ge(a,b):return a >= b


def gt(a,b):return a > b


# MATH AND LOGIC


def not_(obj):return not obj


def truth(obj):return bool(obj)


def is_(a,b):return a is b


def is_not(a,b):return a is not b


abs = abs


def add(a,b):return a + b


def and_(a,b):return a & b


def floordiv(a,b):return a // b


def index(a):return int(a)


def inv(obj):return ~obj


def lshift(a,b):return a << b


def mod(a,b):return a % b


def mul(a,b):return a * b


def neg(obj):return -obj


def or_(a,b):return a | b


def pos(obj):return +obj


def pow(a,b):return a ** b


def rshift(a,b):return a >> b


def sub(a,b):return a - b


def truediv(a,b):return a / b


def xor(a,b):return a ^ b

# SEQUENCES

def concat(a,b):return a + b


def contains(a,b):return b in a


def countOf(a,b):return a.count(b)


def delitem(a,b):
	del a[b]


def getitem(a,b):
	return a[b]


def indexOf(a,b):
	if type(a) is str:return a.find(b)
	else:return a.index(b)


def setitem(a,b,c):
	c[b] = a



# INPLACE

def iadd(a,b): a+=b


def iand(a,b): a&=b


def iconcat(a,b): a+=b


def ifloordiv(a,b): a//=b


def ilshift(a,b): a<<=b


def imod(a,b): a%=b


def imul(a,b): a*=b


def ior(a,b): a|=b


def ipow(a,b): a**=b


def irshift(a,b): a>>=b


def isub(a,b): a-=b


def itruediv(a,b): a/=b


def ixor(a,b): a^=b


b = [4,8,7,6,5]
