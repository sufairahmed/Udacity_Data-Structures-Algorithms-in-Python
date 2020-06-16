def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range (0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                pass
            pass

arr_list = []
len_arr = int(input("take a length of list: "))

for i in range(0,len_arr):
    elements = int(input())
    arr_list.append(elements)

bubble_sort(arr_list)
print("Sorter list: ", arr_list)
