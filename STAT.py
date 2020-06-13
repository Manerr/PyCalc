def mean(data):
 t=0
 for i in sorted(data):t+=i
 return t/len(data)

def harmonic_mean(data):
 n=0
 for i in data:n+=(1/i)
 return len(data)/n

def median(data):
 return mean(data)

def median_low(data):
 s=mean(data)
 t=0
 for i in data:
  if s>=i:t=i
 return t

def median_high(data):
 s=mean(data)
 t=0
 for i in sorted(data,reverse=True):
  if s<=i:t=i
 return t

def mode(data):
 data=sorted(data)
 t=0
 for i in data:
  if data.count(i)>=t:t=i
 return t

def