n = int(input())
s = list(map(int, input().split()))

max_s = max(s)

new_s = []
for i in s:
    new_s1 = (i / max_s) * 100
    new_s.append(new_s1)

av = sum(new_s) / n
print(av)
