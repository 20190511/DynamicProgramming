"""
A36. 편집거리
Goldman Sachs 인터뷰

cat
cut

sunday
saturday


편집거리 : 레벤스테인 (Levensteins Algorithm) 거리 알고리즘
if strA[i] == strB[j]:
  dp[i][j] = dp[i-1][j-1] #아무 연산처리를 하지 않음.
else: dp[i-1][j-1] #교체, dp[i][j-1] #삽입, dp[i-1][j] #삭제
  dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
"""

strA = input() #6
strB = input() #8
lenA,lenB = len(strA),len(strB)
#아이디어. 열값에 j+1 로 초기화를 해주면 어차피 값을 바꾸면서 초기화가 일어나 시간복잡도에 유리하다.
dp = [[j+i for i in range(lenB+1)] for j in range(lenA+1)] #앞이 열, 뒤에가 행 실수에 유의할 것.

for i in range(1, lenA+1):
  for j in range(1, lenB+1):
    if strA[i-1] == strB[j-1]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
print(dp[lenA][lenB])
