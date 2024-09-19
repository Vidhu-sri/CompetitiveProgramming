N = int(input())

for _ in range(N):
    string = input()

    flag = 0
    for i in range(1,len(string)-1):
      
      
        if string[i] == string[i+1]:
            
            print(string[:i+1]+chr(ord(string[i])+1)+string[i+1:])
            flag = 1
            break
    if not flag:
        print(string+chr(ord(string[-1])+1))
    


    [
        [0,5,0,6,0,4,0,7],
        [5,0,2,4,3,0,0,0],
        [0,2,0,1,0,0,0,0],
        [6,4,1,0,0,0,0,0],
        [0,3,0,7,0,0,6,4],
        [4,0,0,0,0,0,3,0],
        [0,0,0,0,6,3,0,2],
        [7,0,0,0,4,0,2,0]
    ]