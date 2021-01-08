import numpy as np

s = str(input())
q = str(input())

b = [[0 for i in range((len(q) + 1))] for j in range(len(s) + 1)]
ans = [0 for i in range(max(len(q),len(s)) + 1)]
r = [0 for i in range(max(len(q),len(s)) + 1)]
for i in range(0, len(s) + 1):
    b[i][0] = i
for i in range(0, len(q) + 1):
    b[0][i] = i

for i in range(1, len(s) + 1):
    for j in range(1, len(q) + 1):
        if (s[i - 1] == q[j - 1]):
            b[i][j] = min(b[i-1][j] + 1, b[i][j - 1] + 1, b[i-1][j-1])
        else:
            b[i][j] = min(b[i - 1][j] + 1, b[i][j - 1] + 1, b[i - 1][j - 1] + 1)
k = b[len(s)][len(q)]
print("Levenshtein distance: " + str(int(k)))
i = len(s)
j = len(q)
s = 0

while (i != 0 and j != 0 and s <= k - 1):
        if (b[i][j] == b[i - 1][j - 1] or b[i][j] == b[i - 1][j - 1] + 1):
            ans[s] = "Z"
            i = i - 1
            j = j - 1
        if (b[i][j] == b[i - 1][j] + 1):
            ans[s] = "U"
            i = i - 1
        if (b[i][j] == b[i][j - 1] + 1):
            ans[s] = "V"
            j = j - 1
        s = s + 1

for i in range(s):
    print(end=ans[i])

