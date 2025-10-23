
#Time complexity O(n^2), space O(1)

arr = [64,2,15,3,2,1,2,3,5,7,8,4454,45]

cont = True

while cont:
	cont = False
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			cont = True
			arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)
