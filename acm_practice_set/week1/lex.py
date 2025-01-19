

n = int(input('enter value'))

binary = list(bin(n)[2:])


for i in range(len(binary)-1,0,-1):
    binary[i-2:i+1] = ['1','0','0']
    print(binary)

print(int(''.join(binary),2))
                  


