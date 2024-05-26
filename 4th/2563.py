## 2563번 색종이 
# 

Paper = [[0]*100 for i in range(100)]
N=int(input())
for i in range(N):
    x,y = map(int,input().split())
    for a in range(10):
        for b in range(10):
            Paper[(x-1)+a][(y-1)+b]=1
            
area = 0

for K in Paper:
   area+=sum(K)
print(area)