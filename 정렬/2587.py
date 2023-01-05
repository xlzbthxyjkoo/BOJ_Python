arr = []
sum = 0
avg = 0

for i in range(5):
  arr.append(int(input()))

for j in range(5):
  sum += arr[j]

avg = sum / 5

median = sorted(arr)


print(int(avg))
print(median[2])
