'''
Codeforces Round 280 
A. Vanya and Cubes
Vanya got n cubes. He decided to build a pyramid from them. Vanya wants to build the pyramid as follows: the top level of the pyramid must consist of 1 cube, 
the second level must consist of 1+2=3 cubes, the third level must have 1+2+3=6 cubes, and so on. 
Thus, the i-th level of the pyramid must have 1+2+...+(i-1)+i cubes.

Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes.

Input
The first line contains integer n (1≤n≤10^4) — the number of cubes given to Vanya.

Output
Print the maximum possible height of the pyramid in the single line.



'''

import sys
n = int(input())
 
if n == 1 or n==2:
    print(1)
    sys.exit(0)
for i in range(1,n):
    if i*(i+1)*(i+2) > 6*n:
        break
print(i-1)
