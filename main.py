"""
A31. 금강
첫째줄에 테스트 케이스 T 입력
매 케이스 테스트마다 
  첫째줄에 n,m (n행 m열) 임을 나타내는 n,m 입력 (1<=n,m<=20)
  둘째 줄에 n x m 개의 위치에 매장된 금의 개수가 공백으로 구별되어있다. (0<=각 위치의 금 개수<=100)

시작점은 1열 어느 곳에나 시작할 수 있고, 매 단계마다 오른쪽, 오른쪽아래, 오른쪽위로만 움직일 수 있다.
ex) 
1 3 3 2
2 1 4 1
0 6 4 7
이라는 금광이 있을 때, 금을 최대로 캘 수 있는 개수는
(1,1)->(2,1)->(3,2)->(3,3)->(3,4) 으로 갈 수 있고 개수는 19개이다.
이 때, 다음 조건에서 가장 금을 많이 캘 수 있는 개수를 출력하시오.

[input]
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

[result]
19
16
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
    