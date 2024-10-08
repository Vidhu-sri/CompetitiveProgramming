
'''
2022-2023 ICPC, NERC, Southern and Volga Russian Regional Contest (Online Mirror, ICPC Rules, Preferably Teams)
M. Minimum LCM

You are given an integer n.

Your task is to find two positive (greater than 0) integers a and b
 such that a+b=n
 and the least common multiple (LCM) of a
 and b
 is the minimum among all possible values of a
 and b
If there are multiple answers, you can print any of them.

Input
The first line contains a single integer t
 (1≤t≤100) — the number of test cases.

The first line of each test case contains a single integer n
 (2≤n≤109).

Output
For each test case, print two positive integers a
 and b
 — the answer to the problem. If there are multiple answers, you can print any of them.

'''


import math
N = int(input())




def largest_divisor(n):
    res = 1
   
    for i in range(int(math.sqrt(n)) ,1,-1):
        if n % i == 0:
      
            res = max(res,n//i)

    return res



for _ in range(N):

    n = int(input())
    res = largest_divisor(n)
    print(res, n-res)


  