"""
A34, 병사배치하기
https://www.acmicpc.net/problem/18353

[풀이]
병사 전투력 중 골칫거리 지수를 설정한다. ( (0...N-1) > N > (N+1 ... end))
해당 부분에서 문제가되는 부분이 몇 개가 있는지 체크해서 가장 문제되는 지점부터 없애면서
모든 지점이 0이 될 때 까지 반복한다.
-> 시간초과
7
15 11 4 8 5 2 4

6
7 3 2 6 5 4

10
11 2 10 6 9 4 3 2 6 5

6
3 5 2 6 1 4 2


[1차풀이]
n = int(input())
corps = list(map(int, input().split()))
checks = [n]*n

count = 0
while True:
  if sum(checks) == 0:
    break
  for i in range(len(corps)):
    if checks[i] == 0:
      continue
    temp = 0
    for front in range(i):
      if corps[front] <= corps[i]:
        temp += 1
    for back in range(i+1,len(corps)):
      if corps[back] >= corps[i]:
        temp += 1
    checks[i] = temp

  del_idx = 0
  temp_idx = -1
  for i in range(len(checks)):
    if temp_idx < checks[i]:
      temp_idx = checks[i]
      del_idx = i
  if sum(checks) == 0:
    break
  corps.pop(del_idx)
  checks.pop(del_idx)
  count += 1

print(count)
"""

"""
풀이 2
가장 긴 부분수열 (LIS) 로 풀이 
if 
7
15 11 4 8 5 2 4 
가장 긴 부분수열로 풀이하면
dp[i] = max(dp[0...i-1])+1 if corps[0...i-1]>corps[i]
"""
n = int(input())
corps=list(map(int,input().split()))

#모든 부분수열은 최소 1이상이므로 1로 설정하고 dp[i] = max(dp[i],dp[j]+1)
#로 해결할 수 있고, 혹은 아래와같이 0으로 설정해두고 나중에 1을 추가하는 방식으로 풀 수 있다.
dp = [0]*n

for i in range(n):
  # tp = dp[0] 빼버리면 0번 인덱스 조건이 안됨
  for j in range(0,i):
    if corps[j] > corps[i]:
      dp[i] = max(dp[i], dp[j])
  dp[i] += 1

#print(dp)
result = n - max(dp)
print(result)

"""
LIS 알고리즘 대표적인 식
모든 o<=j<i 에 대하여 D[i] = max(D[i], D[j]+1) if arr[j]<arr[i]
"""