from collections import Counter
N = int(input())

for _ in range(N):
    n,q = list(map(int,input().split()))
    string1 = input()
    string2 = input()

    for _ in range(q):
        l,r = list(map(int,input().split()))
  
        counter1 = Counter(string1[l-1:r])
        counter2 = Counter(string2[l-1:r])
        res = r-l+1
        count = 0
        for letter in counter1:
            count += max(counter1[letter] - counter2[letter], 0)
        print(count)
