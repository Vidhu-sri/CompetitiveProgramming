t = int(input())


for _ in range(t):
    n = int(input())
    a = (n//15)*3
    if n%15>=2:
        a+=3
    else:
        a+= n%15+1
    print(a)