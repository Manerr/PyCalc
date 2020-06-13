from random import randint as _r

def compare_digest(a,b):return a==b

def choice(sequence):return sequence[_r(0,len(sequence)-1)]
def randbelow(n):return _r(0,n)

def randbits(k):
 n="0b"
 for i in range(k):
  n+=str(_r(0,1))
 return int(n)

def token_bytes(nbytes=None):
 if not nbytes:nbytes=16
 n=b''
 for i in range(nbytes):
  n+="\\x"+str(_r(0,0xff))
 return n

def token_hex(nbytes=None):
 if not nbytes:nbytes=10
 t=""
 for i in range(nbytes):
  t+=str(hex(_r(0,0xff)))[2:]
 return t

def token_urlsafe(nbytes=None):
 if not nbytes:nbytes=16
 t=""
 printable=[i for i in range(48,58)]+[i for i in range(65,91)]+[i for i in range(97,123)]
 for i in range(nbytes):
  c=""
  while c not in printable:
   c=_r(0,255)
  t+=chr(c)
 return t
