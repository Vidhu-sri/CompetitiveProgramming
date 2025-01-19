

def solve(n,b,c):
    high = n
    low = 0

    ans = -1
    def check(k):
        return ((n-k-1)*(b-1)+c == k) or ((n-k-1)*(b-1)+c == k+1)
    
    while high >= low:

        k = (high+low)//2

        if check(k):
            ans = k
            high = k-1
        else:
            low = k+1
    return ans
            
    



N  = int(input())


for _ in range(N):
    n,b,c = tuple(map(int,input().split()))

    print(solve(n,b,c))


