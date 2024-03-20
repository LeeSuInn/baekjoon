n = int(input())

for k in range(n):
    s = input()
    result = []
    strlist = s.split()

    for i in range(len(strlist)):
        if len(strlist[i]) == 1:
                result.append(strlist[i])
        else:
            wordlist = list(strlist[i])
            for j in range(len(strlist[i])//2):
                temp = wordlist[j]
                wordlist[j] = wordlist[-1-j]
                wordlist[-j-1] = temp
            newword = "".join(wordlist)
            result.append(newword)

        output = " ".join(result)
    print(output)