import sys

stR = sys.stdin.readlines()
results = []
for strs in stR:
    result = [0] * 4
    strs = strs[:-1]
    Str = list(strs)

    for c in Str:
        if c.islower():
            result[0] += 1
        elif c.isupper():
            result[1] += 1
        elif c.isdigit():
            result[2] += 1
        else:
            result[3] += 1

    Result = " ".join(map(str,result))
    print(Result)

