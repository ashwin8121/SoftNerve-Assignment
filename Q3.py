# Question 3:Sum of All Subset XOR Totals
from itertools import combinations

def calXorSum(lst):
    xor = 0
    for x in range(len(lst)):
        xor ^=  lst[x]
    return xor

N = int(input())
lst = []
for x in range(N):
    lst.append(int(input()))

xorSum = 0
for x in  range(1, len(lst) + 1):
    combs = list(combinations(lst, x))
    for comb in combs:
        xorSum += calXorSum(comb)

print(xorSum)