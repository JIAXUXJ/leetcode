def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		l = arr[:mid]
		r = arr[mid:]

		mergeSort(l)
		mergeSort(r)

		i = j = k = 0
		while i < len(l) and j < len(r):
			if l[i] < r[j]:
				arr[k] = l[j]
				i += 1
			else:
				arr[k] = r[j]