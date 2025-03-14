
t = int(input())


for _ in range(t):
    n,x,k = map(int,input().split())
    path = input()
    

    #can you go the first time
    #can you come back to zero
    prefix = []
    mov = 0
    for i in range(len(path)):
        mov += 1 if path[i] == 'R' else -1
        prefix.append(mov)

    if -x not in prefix:
        print(0)
        continue
    len1 = prefix.index(-x)+1

    if len1 >k:
        print(0)
    else:
        k-=len1
        if 0 not in prefix:
            print(1)
        else:
            len2 = prefix.index(0)+1
            print(k//len2+1)
    





    



