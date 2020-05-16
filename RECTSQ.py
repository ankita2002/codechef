# cook your dish here
t = int(input())
for i in range (0,t):
  #l = int(input())
  #b = int(input())
  l, b =map(int,input().split())
  x = l*b
  min = x
  for j in range(2,x):
    if l%j==0 and b%j==0:
      a=(l/j)*(b/j)
      if a<=min:
          min =a
  print(int(min))
