import sys

#input()보다 readline()이 더 빠름

N = int(sys.stdin.readline())
arr =[]

for i in range(N):
  arr.append(int(sys.stdin.readline()))

sorted_arr = sorted(arr)

for j in range(N):
  print(sorted_arr[j])
