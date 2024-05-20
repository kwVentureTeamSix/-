w = input().upper()
count = [0]*26

for char in w:
    index = ord(char) - ord('A')
    count[index] += 1

max_N = max(count)
if count.count(max_N) > 1:
    print('?')
else:
    max_index = count.index(max_N)
    max_char = chr(max_index + ord('A'))
    print(max_char)