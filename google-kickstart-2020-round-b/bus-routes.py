def max_start_day(X, D):
  min_day = D
  N = len(X)
  for i in range(N-1, -1, -1):
      x = X[i]
      day = (D // x) * x
      min_day = min(day, min_day)
      D = min_day
  return min_day

t = int(input())
for i in range(1, t + 1):
  n, d = [int(s) for s in input().split(" ")]
  x = [int(s) for s in input().split(" ")]
  print("Case #{}: {}".format(i, max_start_day(x, d)))

