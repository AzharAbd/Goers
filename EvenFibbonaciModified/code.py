def fibb(n, a, b, res):
  if (b % 2 == 0):
    res += b
    
  if (b > n):
    return res
  else:
    return fibb(n-1, b, a+b, res)

def main():
  n = int(input("Enter n value: "))
  print(fibb(n, 0, 1, 0))

main()
