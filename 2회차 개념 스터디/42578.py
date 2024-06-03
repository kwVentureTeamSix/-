## 옷을 안 입는 경우 까지 세준다

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = 1
    for num in cnt.values():
        answer *= (num+1)
    return answer - 1

