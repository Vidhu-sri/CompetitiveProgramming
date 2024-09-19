
n = int(input())

for _ in range(n):
    a,b = input().split()
    string1 = b[0]+a[1:]
    string2 = a[0]+b[1:]
    print(string1,string2)
    
