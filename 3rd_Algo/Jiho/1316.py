def group_word(word):
    checked = []

    for char in word:
        if char not in checked:
            checked.append(char)
        else:
            if checked[-1] != char:
                return False
    return True


N = int(input())
group_words = 0

for _ in range(N):
    word = input().strip()
    if group_word(word):
        group_words += 1

print(group_words)