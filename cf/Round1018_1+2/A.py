

t = int(input())


for _ in range(t):
    n = int(input())
    string = input()

    smol=string.count('<')
    big = n-string.count('>')+1
    res = [smol+1]

    
    


    for i in range(len(string)):
        
        if string[i] == '<':
            res.append(smol)
            smol-=1
        else:
            res.append(big)
            big+=1
    

    print(*res)
