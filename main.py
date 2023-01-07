"""
 Q2. 1로 만들기.
 연산은 4개만 사용할 수 있다.
  1. X가 5의 배수다 -> 5로 나누기
  2. X가 3의 배수다 -> 3으로 나누기
  3. X가 2의 배수다 -> 2로 나누기
  4. X-1

  정수 X가 주어질 때 1로 만들려고 할 때, 연산횟수의 최솟값
  ex) 26->25->5->1 
  result : 3

  [풀이]
  f(N) = mint(f(N-1), f(N/2), f(N/3), f(N/5))+1
  f(1)=0, -> 계속 증가.

  답지와 완전 동일.
"""
x = int(input())
num_count = [0]*(x+1)

for i in range(2, x+1):
  temp = num_count[i-1]
  if (i%2 == 0 and i>=2):
    temp = min(num_count[i//2],temp)
  if (i%3 == 0 and i>=3):
    temp = min(num_count[i//3],temp)
  if (i%5 == 0 and i>=5):
    temp = min(num_count[i//5],temp)
  num_count[i] = temp+1

print(num_count[x])

