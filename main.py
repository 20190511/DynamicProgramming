"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

t = int(input())
results = []
for _ in range(t):
  a, b = map(int, input().split())
  maps = [[] for _ in range(a)]
  lines = list(map(int, input().split()))
  for x in range(a):
    for y in range(b):
      maps[x].append(lines[y+4*x])

  for y in range(1,b):
    for x in range(a):
      temp = maps[x][y-1]
      if (x-1)>=0:
        temp = max(temp, maps[x-1][y-1])
      if (x+1)<a:
        temp = max(temp, maps[x+1][y-1])
      maps[x][y] = temp+maps[x][y]

  result = maps[0][b-1]
  for x in range(1, a):
    result = max(result, maps[x][b-1])
  results.append(result)

for i in range(t):
  print(results[i])
    