#3D prime number 
'''def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5+1)):
        if x % i == 0:
            return False
    return True
n = int(input("Enter number:"))
result = []
i = 2 
while len(result) < n:
    if is_prime(i):
        digit_sum = sum(int(d) for d in str(i))
        digit_count = len(str(i))
        if is_prime(digit_sum) and is_prime(digit_count):
            result.append(i)
    i += 1
print(result)'''
#password
'''n=input("Enter number")
up,dg,sp,lp=0,0,0,0
if len(n)>7:
    for i in n:
        if i.islower():
            lp+=1
        elif i.isupper:
            up+=1
        elif i.isdigit():
            dg+=1
        else:
            sp+=1
    if up>0 and dg>0 and sp>0 and lp>0:
        print("Good password")
    else:
        print("Bad password")
else:
    print("enter the password of length above 7")'''
#spiral matrix
'''a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [30, 31, 32, 13, 14, 15],
     [16, 17, 18, 19, 20, 21],
     [22, 23, 24, 25, 26, 27]]
top = 0
bt = len(a)-1
left = 0
right = len(a[0])-1
while top <= bt and left <= right:
    for i in range(left, right + 1):
        print(a[top][i], end=" ")
    top += 1
    for j in range(top, bt + 1):
        print(a[j][right], end=" ")
    right -= 1
    if top <= bt:
        for k in range(right, left - 1, -1):
            print(a[bt][k], end=" ")
        bt -= 1
    if left <= right:
        for f in range(bt, top-1,-1):
            print(a[f][left], end=" ")
        left += 1'''
#output: 1 2 3 4 5 6 12 15 21 27 26 25 24 23 22 16 30 7 8 9 10 11 14 20 19 18 17 31 32 13 
#Recursion
'''def flower(a):
    if a==4:
        return
    print(a+10,end=" ")
    flower(a+1) #here again a will increment and goes to starting until a==4. and a will be backtracked
    print(a,end=" ")
flower(1)'''
#output:11 12 13 3 2 1 
'''def raju(a):
    if a==1:
        return
    raju(a-1)
    print('hai',end=" ")
    raju(a-1)
raju(5)'''

#output:hai hai hai hai hai hai hai hai hai hai hai hai hai hai hai
'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            for j in range(2,i+1):
                if i%j==0:
                    break
                print(j)
n=int(input("enter the number"))
prime(n)'''
#using two arguments
'''def prime(n,a):
    if n==1:
        return
    i=2
    while n%i!=0:
        i+=1
    print(i,end=" ")
    prime(n//i,a)
n=int(input("enter the number"))
prime(n,2)
'''
#output: 3 5 5
'''s=input().strip()
c=1
r=""
for i in range(len(s)):
       if i+1<len(s) and s[i]==s[i+1]:
        c+=1
       else:
           r=r+s[i]
           r=r+str(c)
           c=1
print(r)'''
#Flames
'''n=input().strip()
k=input().strip()
l1=list(n)
l2=list(k)
f="FLAMES"
l3=list(f)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l1[i]='2'
            l2[j]='2'
print(l1,l2)
x=sum(1 for i in l1 if i!='2')
z=sum(1 for j in l2 if j!='2')
print(x,z)
c=x+z
while len(l3)!=1:
    i=(i+(c-i))%len(l3)
    l3.pop(i)
print(l3)'''

#count
'''a=[1,2,2,2,3,4,5]
c=0
x=sum(1 for i in a if i!=2)
print(x)'''
#finding a number is roundnumber or not
'''def isround(n):
    r=[]
    while n!=1:
        if n in r:
            return False
        r.append(n)
        n=sum(int(i)**2 for i in str(n))
    return True
print(isround(19))'''
#Ranking of students
'''list = [
    {"name": "raju", "age": 28, "marks": [45, 50, 60, 70]},
    {"name": "ravi", "age": 26, "marks": [50, 60, 70, 80]},
    {"name": "ram", "age": 27, "marks": [55, 75, 85, 80]},
]
averages = {}
for student in list:
    name = student["name"]
    marks = student["marks"]
    average = sum(marks) / len(marks)
    averages[name] = average
print(averages)
r=1
for name in averages:
    print(f"{name} has scored {average:.2f} percentage and stands in {r}")
    r+=1'''
#printing pattern 
'''n=int(input("enter number"))
num=1
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,i+1):
            print(num,end=" ")
            num+=1
            if j<i:
                print("*",end=" ")
        print()
    else:
        temp=num+(i-1)
        for j in range(1,i+1):
            print(temp,end=" ")
            if j<i:
                print("*",end=" ")
            temp-=1
            num+=1
        print()'''
#output: 
'''
1 
3 * 2 
4 * 5 * 6 
10 * 9 * 8 * 7 
11 * 12 * 13 * 14 * 15 
21 * 20 * 19 * 18 * 17 * 16 
22 * 23 * 24 * 25 * 26 * 27 * 28 
36 * 35 * 34 * 33 * 32 * 31 * 30 * 29 
37 * 38 * 39 * 40 * 41 * 42 * 43 * 44 * 45 
55 * 54 * 53 * 52 * 51 * 50 * 49 * 48 * 47 * 46 
'''
#running digital clock
'''from datetime import datetime
import pytz
a=pytz.timezone('India/AndhraPradesh')
b=datetime.now(a)
print(b)'''
#running digital clock
'''import time
h=0
m=0
s=0
while 1:
    print(h,':',m,':',s,end='\r')
    time.sleep(1)
    s+=1
    if s==60:
        s=0
        m+=1
    elif m==60:
        m=0
        h+=1
    elif h==24:
        h=0'''
