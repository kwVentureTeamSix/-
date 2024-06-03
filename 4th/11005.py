# 진법 변환 2
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N,B = map(int,input().split())
answer = ''
while N :
    answer = system[N%B] + answer
    N//=B
print(answer)