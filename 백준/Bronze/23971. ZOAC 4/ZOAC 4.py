import math;

w, h, n, m = map(int, input().split())
W = math.ceil(w/(1+n))
H = math.ceil(h/(1+m))
print(W*H)
  