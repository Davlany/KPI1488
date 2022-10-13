def bubble(arr):
	end = len(arr) - 1

	while end != 0:
		for i in range(end):
			if arr[i] < arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]

		end = end - 1

def insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 

def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        max = i
        for j in range(i + 1, len(alist)):
            if alist[j] > alist[max]:
                max = j
        alist[i], alist[max] = alist[max], alist[i]


L = [2,82,6,7,9,12,3,34,23,78,54,55]

part_1 = L[:len(L)>>1]
part_2 = L[len(L)>>1:]


print("Після сортування бульбашкою:")
bubble(part_2)
print(part_2)

print("Після сортування вставкою:")
insert(part_1)
print(part_1)

part_2 = L[len(L)>>1:]

print("Після сортування вибором:")
selection_sort(part_2)
print(part_2)