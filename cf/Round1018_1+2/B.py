
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))

    res = sum(max(pair) for pair in zip(l,r))
    unchosen = sorted([min(pair) for pair in zip(l,r)],reverse=True)
    res+= sum(unchosen[:k-1])+1
    print(res)
    


    


    