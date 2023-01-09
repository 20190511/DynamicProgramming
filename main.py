"""
A33, 퇴사
https://www.acmicpc.net/problem/14501

[풀이]
Top->Down 방식으로 작성.
dp[i] = max(dp[day[i]+i]+pay[i], dp[i+1]) if pay[i]+i-1 <= n

<생각못한 반례 : dp[i+1]은 가능한데 dp[i] 가 Time을 초과하는 경우>
  -> dp[i+1] 이 갱신되었음에도 if문을 거치지 않기 때문에, dp[i] = 0 처리되버린다. 
7
3 10
5 20
1 10
5 20
2 15
4 40
2 200

[반례 피드백]
[풀이 수정 방법론 1 - 조금 난해함]
if 조건 아래에 else에 다음 조건을 추가한다. -> dp[i+1] 값으로 재설정.
  else:
    if i+1 <= n:
      dp[i] = dp[i+1]

[풀이 수정 방법론 2 - 쉬운 방식]
for 문의 max_val 값을 계속 가져가서 if가 안되면 dp[i]=max_val 으로 초기화해준다.
max_val = 0
for문 생략 ...
if day[i]+i-1 <= n:
  dp[i] = max(dp[day[i]+i]+pay[i], max_val)
  max_val = dp[i]
else:
  dp[i] = max_val
  

  

"""
n = int(input())
day = [0]
pay = [0]
for i in range(n):
    d,p = map(int,input().split())
    day.append(d)
    pay.append(p)
    

dp = [0]*(n+2) #dp[i+1] 조건 때문에 1칸 더 늘림.
max_val = 0
for i in range(n,0,-1):
    if day[i]+i-1 <= n:
        dp[i] = max(dp[day[i]+i]+pay[i], dp[i+1])
    else:
        if i+1 <= n:
          dp[i] = dp[i+1]
print(dp[1])
