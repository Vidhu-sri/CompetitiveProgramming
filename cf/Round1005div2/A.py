
t = int(input())

for _ in range(t):
    n = int(input())
    s= input()
    s_new = []
    j = 0
    
    while j<len(s):
        
        prev = s[j]
        while j<len(s) and s[j] == prev :
            j+=1
        s_new.append(prev)
        
    
    res = 0
    if s_new[-1] == '1':
        s_new.pop()
        res+=1
    res+= s_new.count('1')*2
    print(res)

    
    # while i<len(s_new):
    #     if s_new[i] == '1':
    #         res+=1
    #         i+=1
    #     elif i<=len(s_new)-2 and s_new[i] == '0' and s_new[i+1] == '1':
    #         res+=2
    #         i+=2
    #     else:
    #         res+=int(s_new[i])
    #         i+=1
    
   

        
               
    



        
            
        



        


    
