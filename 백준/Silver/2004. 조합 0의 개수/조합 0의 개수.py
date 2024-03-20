def find5(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count

def find2(n):
    count = 0
    while n != 0:
        n //= 2
        count += n
    return count

n , m = map(int, input().split())

five = find5(n) - find5(n-m) - find5(m)
two = find2(n) - find2(n-m) - find2(m)

print(min(five, two))