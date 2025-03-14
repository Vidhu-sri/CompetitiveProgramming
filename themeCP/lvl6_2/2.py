#2021-2022 ICPC, NERC, Northern Eurasia Onsite 
# (Unrated, Online Mirror, ICPC Rules, Teams Preferred)


from collections import Counter
t = int(input())
pos = lambda x: ord(x)-ord('A')


for _ in range(t):
    word,target = input().split()

    w = Counter(word)
    t = Counter(target)

    res = 'YES'

    for l in target:
        if t[l] > w[l]:
            res = 'NO'
            break
    
    word = list(word)
    for l in set(target):
        
        for _ in range(w[l]-t[l]):
            
            word.remove(l)
      
   

    j = 0
    for l in word:
        if j<len(target) and l == target[j]:
            j+=1
    
    print('YES') if j == len(target) else print('NO')





        





        
        
