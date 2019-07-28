def main():
  x = int(input("Enter first number: "))
  y = int(input("Enter second number: "))

  sum = 0
  for i in range(x, y+1):
    sum += i

  res = 0
  for i in range(x, y+1):
    res += i * (sum - i)
  
  print(res)

main()