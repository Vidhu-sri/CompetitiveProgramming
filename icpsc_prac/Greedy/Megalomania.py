'''
Kizahashi, who was appointed as the administrator of ABC at National Problem Workshop in the Kingdom of AtCoder, got too excited and took on too many jobs.
Let the current time be time 
0. Kizahashi has N jobs numbered 1 to N.It takes A i units of time for Kizahashi to complete Job i. The deadline for Job i is time Bi, and he must complete the job before or at this time.

Kizahashi cannot work on two or more jobs simultaneously, but when he completes a job, he can start working on another immediately.

Can Kizahashi complete all the jobs in time? If he can, print Yes; if he cannot, print No.

https://atcoder.jp/contests/abc131/tasks/abc131_d
'''



n= int(input())

tasks = sorted([tuple(map(int,input().split())) for _ in range(n)], key = lambda x:x[1])


elapsed = 0
res = True
for i in range(n):
    elapsed+=tasks[i][0]
    if elapsed > tasks[i][1]:
        res = False
        break
print(res)



    
