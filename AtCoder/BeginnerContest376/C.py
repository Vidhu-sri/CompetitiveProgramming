N = int(input())
toys = list(map(int,input().split()))
box = list(map(int, input().split()))

low ,high = 1,max(toys)
toyz = sorted(toys)
def check(x):

    boxes = sorted(box+[x])
    for i in range(len(boxes)):
        if boxes[i]<toyz[i]:
            return False
    return True


ans = -1
while high>=low:

    mid = (high+low)//2

    if check(mid):
        ans = mid
        high = mid-1
    else:
        low = mid+1
print(ans)
