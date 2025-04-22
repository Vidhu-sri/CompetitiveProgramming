
 
 
t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    
    count,prev = 0,None
 
    for x in string:
        if x != prev:
            prev = x
            count += 1
    
    res = n
 
  
 
    if string[0] == '0':
        if count >= 4:
            res = n + count - 3
        elif count >= 2:
            res = n + 1
        else:
            res = n
    
    if string[0] == '1':
        if count <= 3:
            res = n + 1
        else:
            res = n + count - 2
    
    print(res)