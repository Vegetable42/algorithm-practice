
#Time complexity O(n^2), space O(1)

arr = [64,2,15,3,2,1,2,3,5,7,8,4454,45]
l = len(arr)
for i in range(l):
	for j in range(i+1, l):
		if arr[i] > arr[j]:
			arr[j], arr[i] = arr[i], arr[j]

print(arr)
			
