#loop in for

s='sunday'
for val in range(len(s)):
    print(s[val],end='--')
    
#factors
num=int(input())
for val in range(1,num+1):
    if num%val==0:
        print(f'Factors of {num}',val)
    
#prime numbers
count=0
num=int(input())
for res in range(1,num+1):
    if num%res==0:
        count+=1
if count==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')

#multiplication tables
num=10
for mul in range(1,num+1):
    print(f'{num}*{mul}={num*mul}')

#factorial
num=5
fact=1
if num >=0:
    fact=1
for  res in range(num,0,-1):
    fact*=res
print(fact)

#amstrong number
num=153
sum=0
temp=num
power=len(str(num))
while num!=0:
    rem =num%10
    sum=sum+rem**power
    num=num//10
print(sum)
if sum == temp:
    print('Amstrong Number')
else:
    print('Not an Amstrong')
#Disarium Number
num=135
temp=num
sum=0
power=len(str(num))
while num!=0:
    rem=num%10
    sum=sum+rem**power
    power=power-1
    num=num//10
print(sum,num,temp)
if sum==temp:
    print('disarium number')
else:
    print('Not a disrium number ')
    
#Spy Number
num=123
sum=0
temp=num
prod=1
while num!=0:
    rem=num%10
    sum=sum+rem
    prod=rem * prod
    num=num//10
print(sum,num,prod)
if sum==prod:
    print('its a spy number')
print('not a Spy Number')

#LCM of two numbers
n1=int(input())
n2=int(input())
if n1> n2:
    lcm=n1
else:
    lcm=n2
while True:
    if(n1%lcm==0 and n2%lcm==0):
        print(lcm)
        break
    else:
        lcm+1
for row  in range(1,6):
    for col  in range(1,6):
        print('*',end=' ')
    print()

num=4
for row in range(1,num+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()
num=5
col=1
row=1
while row<num+1:
    col=1
    while col<row+1:
        print('* ',end=' ')
        col+=1
    print()
    row+=1        




    


    

