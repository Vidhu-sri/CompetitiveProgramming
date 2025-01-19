import bisect
def fibs(n):
    nums = [0,1]

    while nums[-1] <= n:
        num = nums[-1]+nums[-2]
        nums.append(num)
    while nums and nums[-1] > n:
        nums.pop()
    return nums

big_fib = lambda x,nums: bisect.bisect_right(nums,x)-1


def solve(n):

    if not n:
        return []
    nums = fibs(n)

    to_subtract = nums[big_fib(n,nums)]
    res = [to_subtract]
    res+= solve(n-to_subtract)
    return res


n= int(input())
print(solve(n))


