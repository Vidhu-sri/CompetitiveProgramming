t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    nums.sort()
    i,j = 0,n-1

    even_odd= [1 if num%2==0 else 0 for num in nums]

    val1 = even_odd[i]
    val2 = even_odd[j]
    if val1 == val2:
        print(0)
        
    else:
        while even_odd[i] != val2:
            i+=1
        while even_odd[j] != val1:
            j-=1
        print(min(i,n-1-j))

        

    

        
