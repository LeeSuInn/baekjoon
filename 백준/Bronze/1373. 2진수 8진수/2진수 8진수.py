n = input()

rest = ((len(n)) % 3)
result = ""

if rest != 0:
    for i in range(3 - rest):
        n = "0" + n

for i in range(0,len(n),3):
    result += (str)((int(n[i]) * 4) + (int(n[i + 1]) * 2) + (int(n[i + 2]) * 1))

print(result)
