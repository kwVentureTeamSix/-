# 진법 변환


system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N,B = map(str,input().split())
B = int(B)
answer = 0
for i, num in enumerate(N):
    ## 1100 2 
    answer += B ** (len(N)-(i+1)) *system.index(num)
print(answer)