s =[]
for i in range(1,31):
    s.append(i)

for _ in range(28):
    s.remove(int(input()))

print(s[0])
print(s[1])
