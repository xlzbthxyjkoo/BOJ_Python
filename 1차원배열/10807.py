N = int(input())
arr = list(map(int,input().split()))
v = int(input())

cnt = 0
for j in range(N):
    if arr[j] == v:
        cnt += 1

print(cnt)
