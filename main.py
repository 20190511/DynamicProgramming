"""
dp[i][j] = max(dp[i-1][j-1], dp[i][j]) + tri[i][j]
"""
n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(tri[i])):
        val = tri[i][j]
        if j-1 >= 0:
            tri[i][j] = max(tri[i-1][j-1]+val, tri[i][j])
        if j < len(tri[i-1]):
            tri[i][j] = max(tri[i-1][j]+val, tri[i][j])

result = max(tri[n-1])
print(result)
