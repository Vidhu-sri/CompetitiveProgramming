

t = int(input())

for _ in range(t):

    string = input()
    stack = []

    empties = 0
    for i in range(len(string)):

        if string[i] == '(':
            stack.append('(')
        else:
            stack.pop()
        

        if not stack:
           
            print('NO') if i==len(string)-1 else print('YES')
            break
               
            
            