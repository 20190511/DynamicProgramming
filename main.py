"""
10
1 5 8 9 2 9 10 24 35 21
6
1 3 1 5 7 9

30
1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21

60
1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21

90
1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21 1 5 8 9 2 9 10 24 35 21

4
1 3 1 5
[idea]
 다익스트라처럼, food 배열을 하나 다시 만들어서
  check[N] 이면 N까지 왔을 때 가장 큰 값을 비교해서 갱신하는 방식으로 접근해보자.

  ex) f는 계속 해서 최댓값으로 갱신.
  f(5) = max(f(3)+food[5], f(2)+food[5], f(1)+food[5])
  f(n) = max(f(1~n-2) + food[5])
"""

n = int(input())
food = list(map(int, input().split()))
check = [-1]*n
check[0], check[1] = food[0], food[1]

def attack(food, check, x):
  if x == 0 or x == 1:
    return check[x]

  if check[x] != -1:
    return check[x]
    
  val_list = check[0]+food[x]
  for i in range(1, x-1):
    temp = attack(food, check, i)+food[x]
    if val_list < temp:
      val_list = temp
  check[x] = val_list
  return check[x]

#n-2번도 시행해줘야한다. 2칸씩 건너뛰면서 값이 정해져서 이전값이 갱신안될 수 있음.
attack(food, check, n-1)
attack(food, check, n-2) 
print(max(check[-1],check[-2]))



"""
 실제로는, D[i] = D[i-1] 과 D[i-2]+food[i] 중 큰 값만 비교하면 구할 수 있다.
  (D[i-2]에서 이미 D[i-2] 까지의 최댓값을 구했기 때문이다.)

d[0] = food[0]
d[1] = max(food[1], d[0])
for i in range(2,n):
  d[i] = max(d[i-1], d[i-2]+food[i])
print(d[n-1])

"""