n = int(input())
result = []
for i in range(n):
    word = input()
    if word in result:
        continue
    result.append(word)

Result = sorted(result)
Result.sort(key = len)


RESULT = "\n".join(Result)
print(RESULT)