import sys
from collections import deque
import heapq
 
t=int(input())
for _ in range(t):
    s,r=map(str,input().split())
    s=int(s)
    r=list(r)
    for i in range(len(r)):
        print(r[i]*s,end='')
    print('')