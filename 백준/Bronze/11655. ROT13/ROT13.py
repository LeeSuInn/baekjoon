Str = list(input())
result = ""
for c in Str:
    if c.islower():
        if ord(c) + 13 > 122:
            c = chr(ord(c) - 13)
        else:
            c = chr(ord(c) + 13)
    elif c.isupper():
        if ord(c) + 13 > 90:
            c = chr(ord(c) - 13)
        else:
            c = chr(ord(c) + 13)    
            
    result += c
print(result)