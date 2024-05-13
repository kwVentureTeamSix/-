a=[0]*10
mod=set()
for i in range(0,10):
  a[i]=int(input())
  mod.add(a[i]%42)
print(len(mod))