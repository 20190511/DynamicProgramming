"""
Q5. 효율적인 화폐 구성 (p.226)
N종류의 화폐가 있을 때,
  M원을 만들기 위한 최소 화폐수를 구하여라.

첫 줄에 N원 (1<=N<=100 , 1<=M<=10,000)
둘째줄부터 화폐 종류가 들어온다.

[풀이]
화폐 : a1,a2,...,an
f(n) = min(f(n-a1), f(n-a2), ... , f(n-an)) + 1

[input]
2 15
2
3

3 4
3
5
7

3 7
2
3
5
----
[result]
5

-1

<피드백>
dp = [-1]*(10001) 해당 부분은
2번 풀이에서 coin_list 의 코인 가치가 구하려는 값보다 큰 경우
out of index 를 초래할 수 있기 때문에
[-1]*(m+1) 를 사용할 수 없음.
"""
n,m = map(int,input().split())
coin_list = []
dp = [-1]*(10001) # 2번 풀이에서 m보다 coin_list가 더 커서 오류 발생할 수 있음

for i in range(n):
  co = int(input())
  coin_list.append(co)
  dp[co] = 1

dp[0] = 0 #i-coin = 0 인
max_coin = max(coin_list)
for i in range(1, m+1):
  min_val = 101
  for coin in coin_list:
    if i>=coin and dp[i-coin] != -1:
      if min_val > dp[i-coin]:
        min_val = dp[i-coin]
  if min_val != 101:
    dp[i] = min_val+1

print(dp[m])
print(dp[1:m+1])


"""
[풀이]
  :화폐를 기준으로 화폐1개를 고정시켜두고 1~m번까지 쭉 돌리는 기법을 사용.

  d = [10001]*(m+1)

  d[0] = 0
  for i in range(n):
    for j in range(array[i],m+1):
      if d[j-array[i]] != 10001:
        d[j] = min(d[j],d[j-array[i]]+1)
  if d[m] == 10001:
    print(-1)
  else:
    print(d[m])



"""