N=int(input())
count = 0
for i in range(N):
  word = input()
  ## 이미 나왔던 것
  exist = set()
  last = word[0]
  exist.add(last)
  is_group_word = True
  for i in range(1,len(word)):
    ## 현재 문자
    current = word[i]
    ## 이미 존재하는 문자
    if current in exist:
        ## 저번 문자와 같지 않다면
        if current != last:
            is_group_word = False
            break
    else:
        exist.add(current)
    last = current
  if is_group_word:
        count += 1
print(count)

