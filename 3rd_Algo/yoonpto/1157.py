word=input().lower() #mississipi baaa
cnt=[]
lis=list(set(word)) #misp / ba
for i in lis:
  count=word.count(i)
  cnt.append(count) # 4 4 1 1 / 1 3
if cnt.count(max(cnt))>=2: #최대값이 여러개
  print('?')
else: 
  print(lis[(cnt.index(max(cnt)))].upper()) 
 # 