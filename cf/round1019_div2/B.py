import re
t = int(input())


inverse = lambda x:'1' if x=='0' else '0'
def cost(string):
    curr = 0
    res =  0
    for i in range(len(string)):
        if string[i] !=curr:
            res+=2
            curr =  inverse(curr)
        else:
            res+=1
    return res-1


for _ in range(t):
    n = int(input())
    string = input()
    searched =  re.search(r'1+0+',string)

    if searched:
        i,j = searched.span()

        string =string[:i]+string[i:j][::-1]+string[j:]
  
    print(cost(string))

    
        
