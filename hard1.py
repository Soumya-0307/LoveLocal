def printMax(arr, N, K):
	max = 0

	for i in range(N - K + 1):
		max = arr[i]
		for j in range(1, K):
			if arr[i + j] > max:
				max = arr[i + j]
		print(str(max) + " ", end="")

if __name__ == "__main__":
	arr = [1,3,-1,-3,5,3,6,7]
	N = len(arr)
	K = 3
	

	printMax(arr, N, K)


