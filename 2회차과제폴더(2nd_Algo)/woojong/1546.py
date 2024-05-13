N=int(input())
a=list(map(int,input().split()))
sum=0
max_num=max(a)
for i in a:
  sum+=(i/max_num*100)
print(sum/N)
