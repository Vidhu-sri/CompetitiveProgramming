def is_subsequence(word, letters):
    index = 0
    for char in letters:
        if index < len(word) and char == word[index]:
            index += 1
    return index == len(word)

word = "DONATION"
letters = ['D', 'E', 'S', 'U', 'O', 'N', 'L', 'Z', 'A', 'T', 'I', 'O', 'N']

if is_subsequence(word, letters):
    print("'DONATION' appears in order")
else:
    print("'DONATION' does not appear in order")
