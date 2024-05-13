r = set()

for _ in range(10):
    num = int(input())
    r.add(num % 42)

print(len(r))