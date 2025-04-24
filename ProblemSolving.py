#3D prime number

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5+1)):
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
    i += 1
print(result)

#password

n=input("Enter number")
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
    print("enter the password of length above 7")
    
#spiral matrix

a = [[1, 2, 3, 4, 5, 6],
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
        left += 1
        
Output:
1 2 3 4 5 6 12 15 21 27 26 25 24 23 22 16 30 7 8 9 10 11 14 20 19 18 17 31 32 13

#Recursion

def flower(a):
    if a==4:
        return
    print(a+10,end=" ")
    flower(a+1)
    print(a,end=" ")
flower(1)

Output: 11 12 13 3 2 1
#

def raju(a):
    if a==1:
        return
    raju(a-1)
    print('hai',end=" ")
    raju(a-1)
raju(5)
Output: hai hai hai hai hai hai hai hai hai hai hai hai hai hai hai

#prime logic

def prime(n):
    for i in range(2,n):
        if n%i==0:
            for j in range(2,i+1):
                if i%j==0:
                    break
                print(j)
n=int(input("enter the number"))
prime(n)
#using two arguments

def prime(n,a):
    if n==1:
        return
    i=2
    while n%i!=0:
        i+=1
    print(i,end=" ")
    prime(n//i,a)
n=int(input("enter the number"))
prime(n,2)
Output: 3 5 5

#String compression

s=input().strip()
c=1
r=""
for i in range(len(s)):
       if i+1<len(s) and s[i]==s[i+1]:
        c+=1
       else:
           r=r+s[i]
           r=r+str(c)
           c=1
print(r)
#Flames

n=input().strip()
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
print(l3)
#count elements

a=[1,2,2,2,3,4,5]
c=0
x=sum(1 for i in a if i!=2)
print(x)
#finding a number is roundnumber or not

def isround(n):
    r=[]
    while n!=1:
        if n in r:
            return False
        r.append(n)
        n=sum(int(i)**2 for i in str(n))
    return True
print(isround(19))
#Ranking of students

list = [
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
    r+=1
#printing pattern

n=int(input("enter number"))
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
        print()
#running digital clock

from datetime import datetime
import pytz
a=pytz.timezone('India/AndhraPradesh')
b=datetime.now(a)
print(b)
#running digital clock

import time
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
        h=0
#Global variable is classified into two variables one is instance(non-static) and class(static).

#giving user input at compile time.

class Student:
    def marks(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def average(self):
        average=(self.m1+self.m2)/2
        return average

n=int(input("enter no of students"))
l=[]
for i in range(n):
    r=Student()
    m1=int(input("enter the marks of student{}".format(i+1)))
    m2=int(input("enter the marks of student{}".format(i+1)))
    r.marks(m1,m2)
    l.append(r)

index=0
for i in l:
    index+=1
    res=i.average()
    print("Average of student {} is {}".format(index,res))
#implementation of singly linked list

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Linkedlist:
        def __init__(self):
             self.Head=None
        def insert(self,val):
            if not self.Head:
                  new_node=Node(val)
                  self.Head=new_node
            else:
                temp=self.Head
                while temp.next:
                      temp=temp.next
                new_node=Node(val)
                temp.next=new_node
            print("{} is successfully inserted".format(val))
        def display(self):
            res=[]
            temp=self.Head
            while temp:
                 res.append(temp.val)
                 temp=temp.next
            print("->".join(map(str,res)))
        def delete(self,val):
            temp=self.Head
            prev=None
            while temp:
                 if temp.val==val:
                      if prev:
                           prev.next=temp.next
                      else:
                           self.Head=temp.next
                      print("{} is successfully deleted".format(val))
                      return
                 prev=temp
                 temp=temp.next
            print("{} not found on list".format(val))

r=Linkedlist()
r.insert(100)
r.insert(200)
r.insert(300)
r.insert(400)
r.display()
r.delete(int(input("Enter number to delete: ")))
#output
100 is successfully inserted
200 is successfully inserted
300 is successfully inserted
400 is successfully inserted
100->200->300->400

#Evaluating the Expression

def evaluate(s):
    nums = []
    symbol = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    def apply_op():
        op = symbol.pop()
        right = nums.pop()
        left = nums.pop()
        if op == '+':
            nums.append(left + right)
        elif op == '-':
            nums.append(left - right)
        elif op == '*':
            nums.append(left * right)
        elif op == '/':
            nums.append(left / right)

    i = 0
    while i < len(s):
        if s[i].isdigit():
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            nums.append(int(num_str))
            continue
        elif s[i] in precedence:
            while symbol and precedence[symbol[-1]] >= precedence[s[i]]:
                apply_op()
            symbol.append(s[i])
            i += 1
        else:
            i += 1

    while symbol:
        apply_op()

    return nums[0]

n = "10+2/3+4-2"

#Checking valid parenthesis

'''class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping: 
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:  
                stack.append(char)

        return not stack'''
#Task Scheduling using round robin method
'''from collections import deque
def find(tasks,time_slice):
    Q=deque()
    for i in range(len(tasks)):
'''

#Printing the data of students in table format.

'''students={1:{"name":"sridhar","age":20,"gen":"male","dept":"CSE"},
          2:{"name":"sridharreddy","age":20,"gen":"male","dept":"CSE"},
          3:{"name":"sridhar","age":20,"gen":"male","dept":"CSE"},
          4:{"name":"sridhar","age":20,"gen":"male","dept":"CSE"}}
print("-"*45)
print("{:<5}|{:<15}|{:<7}|{:<7}|{:<7}|".format("ID","NAME","AGE","GEN","DEPT"))
print("-"*45)
for id,info in students.items():
    print("{:<5}|{:<15}|{:<7}|{:<7}|{:<7}|".format((id),info["name"],info["age"],info["gen"],info["dept"]))'''
#output:
'''
---------------------------------------------
ID   |NAME           |AGE    |GEN    |DEPT   |
---------------------------------------------
1    |sridhar        |20     |male   |CSE    |
2    |sridharreddy   |20     |male   |CSE    |
3    |sridhar        |20     |male   |CSE    |
4    |sridhar        |20     |male   |CSE    |
'''

#finding day

'''import calendar
d=calendar.weekday(2025,4,24)
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days[d])'''
#finding how many days you lived
'''from datetime import date
birth_date = date(2004, 11, 16)  
today = date.today()
days_lived = (today - birth_date).days
print(f"You have lived {days_lived} days.")'''

#

'''from collections import deque
n= [1,3,-1,-3,5,3,6,7]
k = 3
Q=deque()
i=0
res=[]
while i<len(n):
    Q.append(i)
    if len(Q)<=3:
        l=max(Q)
        res.append(l)
    Q.popleft()
print(res)'''

#mind game

'''import random
name1=input("enter player 1")
name2=input("enter player 2")
print("computer has fixed 5 number of integers in its mind")
print("you both have 3 chances to guess it")
print("Ready for the game")
random_number = random.randint(1, 11)
print("Random number:", random_number)
r= [random.randint(1, 11) for _ in range(1,11)]
s=set(r)
print("List:", s)
s1=0
s2=0
p1=[]
p2=[]
for i in range(1,4):
    f=int(input("enter the choice {} of {}".format(i,name1)))
    if f in p1:
        print("Already Choosen")
        f=int(input())
    if f in s:
        print("correct")
        s1+=1
    else:
        print("wrong")
    g=int(input("enter the choice {} of {}".format(i,name2)))
    if g in p2:
        print("Already Choosen")
        g=int(input())
    if g in s:
        print("correct")
        s2+=1
    else:
        print("wrong")
if s1>s2:
    print("{} is the winner".format(name1))
elif s1<s2:
    print("{} is the winner".format(name2))
else:
      print("it is tie")'''
r = evaluate(n)
print(int(r))


