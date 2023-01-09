"""
A35. 못생긴수 P.381


[시간초과 풀이]
import time
start = time.time()
n = int(input())
dp = [1]*n
for i in range(1,n):
  pivot = dp[i-1]
  dp[i] = pivot*5
  j = 0
  while j < i:
    if pivot < dp[j]*2:
      dp[i] = min(dp[i], dp[j]*2)
      break
    if pivot < dp[j]*3:
      dp[i] = min(dp[i],dp[j]*3)
    if pivot < dp[j]*5:
      dp[i] = min(dp[i],dp[j]*5)
    j += 1
end = time.time()
print(dp[n-1])
print(end-start)
  """
n = int(input())
ugly = [0]*n
ugly[0] = 1

i2 = i3 = i5 = 0
next2,next3,next5 = 2,3,5
for i in range(1,n):
  ugly[i] = min(next2,next3,next5)
  if ugly[i] == next2:
    i2 += 1
    next2 = ugly[i2]*2 #ugly[i2+1]*2 다음값*2 로 초기화.
  if ugly[i] == next3:
    i3 += 1
    next3 = ugly[i3]*3
  if ugly[i] == next5:
    i5 += 1
    next5 = ugly[i5]*5
print(ugly[n-1])
"""
[피드백]
next2,next3,next5 중 최솟값을 구하고 
해당 값의 index를 +1해준 값의 *n을 해주며 이 과정을 반복한다.
i2,i3,i5 가 해당될 때 마다 0에서부터1씩 늘려가며 ugly[i2(0...->)] * 2 씩 곱한 값을
"""
