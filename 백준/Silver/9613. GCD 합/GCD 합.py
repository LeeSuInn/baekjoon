import sys
from math import gcd
n = int(input())

for i in range(n):
    result = 0
    numli = input().split(" ")

    for j in range(1, int(numli[0])):
        for k in range(j + 1,int(numli[0]) + 1):
            result += gcd(int(numli[j]), int(numli[k]))

    print(result)
