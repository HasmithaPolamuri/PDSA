#Using a separe list
def gcd(m,n):
  cf=[]      #List of common factors
  for i in range(1,min(m+n)+1):     #gcd is less than or equal to smaller number
    if ((m%i)==0 and (m%i)==0):
      cf.append(i)
  return(cf[-1])  #returns the highest common factor


#Without creating a list
def gcd(m,n):
  for i in range(1,min(m+n)+1):     #gcd is less than or equal to smaller number
    if ((m%i)==0 and (m%i)==0):
      cf=i  #updates i to most recent common factor
  return(cf) 
