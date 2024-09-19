N = int(input())


for _ in range(N):
    
    l,r = list(map(int,input().split()))
    L,R  = list(map(int,input().split()))

    if L > r or l>R:
        print(1)
    else:
        bigger = (L,R) if R>=r else (l,r)
        smaller = (l,r) if R>=r else (L,R)

        toadd = (bigger[1]!=smaller[1]) + (bigger[0]!=smaller[0])

        overlap_left = smaller[0] if smaller[0] > bigger[0] else bigger[0]

        print(toadd+smaller[1]-overlap_left) 


