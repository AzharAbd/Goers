def countSum(x, n):
  sum = 0
  for i in range(n):
    sum += x * (i+1)
  return sum

def gcd(a, b):
  if (a % b == 0):
    return b
  else:
    return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

def main():
  x = int(input("Enter first value: "))
  y = int(input("Enter second value: "))
  n = int(input("Enter n value: "))
  n -= 1
  k = lcm(x, y)
  
  res = countSum(x, (n // x)) + countSum(y, (n // y)) - countSum(k, (n // k))
  print(res)

main()