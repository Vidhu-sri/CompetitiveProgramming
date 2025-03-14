from collections import defaultdict


t = int(input())


for _ in range(t):
   
    string = input()

    left = defaultdict(int)
    right = defaultdict(int)


    i,j = 0,len(string)-1

    while j>i and string[i] == string[j] :
        i+=1
        j-=1
    if i>j:
        print(0)
        continue

    left[string[i]]+=1
    right[string[j]]+=1

    while left != right:
        i+=1
        j-=1
        left[string[i]]+=1
        right[string[j]]+=1
    