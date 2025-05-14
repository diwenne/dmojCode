word = input()

def check(substr):
    for i in range(len(substr)//2):
        # print(substr[i],substr[-i-1])
        if substr[i] != substr[-i-1]:
            return False
    return True

def all_consecutive_substrings(s):
    n = len(s)
    substrings = []

    for start in range(n):
        for end in range(start + 1, n + 1):  # end goes from start+1 to n (inclusive)
            substrings.append(s[start:end])

    return substrings

substrings = all_consecutive_substrings(word)
maxlen = 0
for i in substrings:
    if check(i):
        maxlen = max(maxlen,len(i))

print(maxlen)