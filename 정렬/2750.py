num = int(input()) 
arr = []

for i in range(num):
    arr.append(int(input()))

sorted_arr = sorted(arr) #정렬

for i in range(num):
    print(sorted_arr[i])
