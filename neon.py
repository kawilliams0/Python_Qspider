n=9
sq=n**2
sum1=0
while sq!=0:
    sum1+=sq%10
    sq//=10
print("Yes" if sum1==n else "no")
