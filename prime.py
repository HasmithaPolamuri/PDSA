#Checking if a number is prime
def factors(n):
  f1=[]
  for i in range(1,n+1):
    if (n%i)==0:
      f.append(i)
  return(f)

def prime(n):
  return(factors(n)==[1,n])  #checks if list of factors is equal to prime factors list  and returns prime or not

#Different approach
def prime(n):
  result=True
  for i in range(2,n):
    if(n%i)==0:
      result=False
  return result


#List of all prime upto m
def primes_upto_m(m):
  pl=[]
  for i in range(2,m+1):
    if prime(i):
      pl.append(i)
  return(pl)


#list of first m primes
def first_m_primes(m):
  (count,i,pl)=(0,1,[])
  while count<m:
    if prime(i):
      (count,pl)=(count+1,pl+[i])
      i=i+1
return pl
