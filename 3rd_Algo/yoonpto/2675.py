test=int(input())
for i in range(test):
  N,word=input().split()
  N=int(N)
  for k in word:
    print(k*N,end="")
  print()