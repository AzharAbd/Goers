import math 
  
def main():
  n = int(input("Enter n value: "))
  res = -1
    
  while n % 2 == 0: 
    res = 2
    n >>= 1    

  for i in range(3, int(math.sqrt(n)) + 1, 2): 
    while n % i == 0: 
      res = i 
      n = n / i 

  if n > 2: 
    res = n 
    
  print(int(res))

main() 