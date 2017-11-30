'''Warmup Challenges'''

'''Solve Me First'''
def solveMeFirst(a,b):
   # Hint: Type return a+b below
    return a+b


num1 = input()
num2 = input()
res = solveMeFirst(num1,num2)
print res

'''Simple Array Sum'''
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print sum(arr)

'''Compare the Triplets'''
import sys
def comp(A,B):
    sb=0
    sa=0
    for i in range(len(A)):
        if A[i]>B[i]:
            sa+=1
        elif A[i]==B[i]:
            sa+=0
            sb+=0
        else:
            sb+=1
    return sa,sb

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
A=[a0,a1,a2]
B=[b0,b1,b2]
sa, sb = comp(A,B)
print sa, sb

'''A Very Big Sum'''
import sys


def aVeryBigSum(n, ar):
    return sum(ar)


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

'''Diagonal Difference'''
import sys
n = int(input().strip())
a = []
diag1=[]
diag2=[]
for i in range(n):
    arr=input().split()
    diag1 += [int(arr[i])]
    diag2 += [int(arr[n-i-1])]
print(abs(sum(diag2)-(sum(diag1))))

'''Plus Minus'''
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos=[]
neg=[]
zer=[]
for i in arr:
    if i>0:
        pos+=[i]
    elif i<0:
        neg+=[i]
    else:
        zer+=[i]
print("%.6f" % (len(pos)/n))
print("%.6f" % (len(neg)/n))
print("%.6f" % (len(zer)/n))

'''Staircase'''
import sys
n = int(input().strip())
for i in range(1,n+1):
    print(" "*(n-i) + i*"#")

'''Mini-Max Sum'''
import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
print(sum(arr[:4]), sum(arr[1:]))

'''Birthday Cake Candles'''
import sys

def birthdayCakeCandles(n, ar):
    ma = max(ar)
    return (ar.count(ma))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

'''Time Conversion'''
import sys
def timeConversion(s):
    time = s[:-2]
    h = int(time[:2])
    if h<12 and s[-2:]=='PM':
        d = h+12
        time = time[2:]
        return  (str(d)+time)
    elif h==12 and s[-2:]=='AM':
        d = h-12
        return (str(d)+'0' + time[2:])
    elif h==12 and s[-2:]=='PM':
        return(time)
    else:
        return(time)
s = input().strip()
result = timeConversion(s)
print(result)


'''Strings Challenges'''

'''CamelCase'''
import sys
s = list(input().strip())
c = 0
for el in s:
    if el.isupper() == True:
        c += 1
print(c+1)

'''Two Characters'''
import sys
from itertools import combinations

def meet_pattern(s):
    return all(s[i-1] != s[i] for i in range(1,len(s)))

s_len = int(input().strip())
s = input().strip()
letters = set(s)
max_len = 0
for pair in combinations(letters,2):
    substr = "".join(i for i in s if i in pair)
    if meet_pattern(substr):
        max_len = max(max_len, len(substr))
print(max_len)

'''Caesar Cipher'''
import sys
n = int(input().strip())
s=str(input().strip())
k = int(input().strip())
for i in s:
    a=65 if i.isupper() else 97
    print((chr(a+(ord(i)-a+k)%26)) if i.isupper() or i.islower() else i ,end='')

'''Mars Exploration'''
import sys
altered=0
inp = input().strip()
for i in range(len(inp)):
    x=i%3
    if(x==0 and inp[i]!='S'):
        altered+=1
    elif(x==1 and inp[i]!='O'):
        altered+=1
    elif(x==2 and inp[i]!='S'):
        altered+=1
print(altered)

'''Sherlock and Anagrams'''
import sys

test = int(input())
for _ in range(test):
    string = input().strip()
    n = len(string)
    substring = [''.join(sorted(string[i:j + 1])) for i in range(n) for j in range(i, n)]
    answer = 0
    substring.sort(key=len)
    substring.sort()

    i = 0
    while i < len(substring):
        temp = substring.count(substring[i])
        answer += (temp * (temp - 1)) // 2
        i += temp
    print(answer)


'''Sorting Challenges'''

'''Big Sorting'''
import sys
import collections as c

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

d = c.defaultdict(list)

for i in unsorted:
    d[len(i)].append(i)

for key in sorted(d.keys()):
    print(*sorted(d[key]), sep='\n')

'''Intro to Tutorial Challenges'''
v = str(int(input()))
n = int(input())
ar = list(input().strip().split())
print (ar.index(v)

'''Correctness and the Loop Invariant'''
n,m=input(),list(map(int, input().strip().split()))
m.sort()
print(*m, sep=" ")

'''Running Time of Algorithms'''


def insertion_sort(l):
    count = 0
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            count += 1
            j -= 1
        l[j + 1] = key
    return count


m = input()
l = [int(i) for i in input().strip().split()]
print(insertion_sort(l))

'''Quicksort 1 - Partition'''


def partition(ar):
    p = ar[0]
    eq, left, right = [], [], []
    for i in ar:
        if i >= p:
            right.append(i)
        elif i < p:
            left.append(i)
    for t in left:
        print(t, end=" ")
    for k in right:
        print(k, end=" ")

    return ""


m = input()
ar = [int(i) for i in input().strip().split()]
print(partition(ar))

'''Counting Sort 1'''
s = input()
a =list(map(int, input().strip().split(' ')))
d = []
for  i in range(100):
    if i in a:
        r = a.count(i)
        d+=[r]
    else:
        d+=[0]
print(*d)

'''Counting Sort 2'''
s = input()
a =list(map(int, input().strip().split(' ')))
d = sorted(a)
for i in d:
    print (i, end = " ")

'''The Full Counting Sort'''
n = int(input())
ar = []
for i in range(n):
    if i < n//2:
        numX, striX = input().strip().split()
        ar.append((int(numX),'-'))
    else:
        numX,striX = input().strip().split()
        ar.append((int(numX),striX))

ar.sort(key=lambda tup: tup[0])
print(*[x[1] for x in ar])

'''Closest Numbers'''
n, l = int(input()), list(map(int, input().split()))
l.sort()
diff = [abs(l[i]-l[i+1]) for i in range(n-1)]
m = min(diff)
for i in range(len(diff)):
    if m==diff[i]:
        print(l[i], end=' ')
        print(l[i+1], end=' ')

'''Find the Median'''
import statistics
int(input())
arr = list(map(int, input().strip().split(' ')))
print(statistics.median(arr))