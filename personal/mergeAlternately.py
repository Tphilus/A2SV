def mergeAlternately(word1, word2):
    result = []

    # Use the two pointer to iterate through both strings
    i = j = 0
    while i < min(len(word1), len(word2)):
        result.append(word1[i] + word2[i])
        i += 1

    result.append(word1[i:])
    result.append(word2[i:])

    # convert the arr to string
    return "".join(result)

word1 = []
word2 = []
print(mergeAlternately(word1, word1))