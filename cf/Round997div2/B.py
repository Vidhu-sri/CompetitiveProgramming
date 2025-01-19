
from collections import defaultdict
N = int(input())


#small i have edge with, big i dont have edge with

def idx(adj,i,j):

    return (i>j and j in adj[i]) or (i<j and j not in adj[i])

for _ in range(N):
    n = int(input())

    adj = defaultdict(set)
    res = [0]*n
    for i in range(1,n+1):
        neighbors = input()
        for j in range(len(neighbors)):
            if neighbors[j] == '1':
                adj[i].add(j+1)
        

    
    for i in range(1,n+1):
        index = 0
        for j in range(1,n+1):
            index += idx(adj,i,j)
        res[index] = i
    print(*res)



        

    

    
    
    
        



