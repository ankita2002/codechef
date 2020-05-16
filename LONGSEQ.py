# cook your dish here
t = int(input())
for i in range (0,t):
    num = input()
    a = num.count('1')
    b = num.count('0')
    if a==1 or b==1:
        print("Yes")
    else:
        print("No")
