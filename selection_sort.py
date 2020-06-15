def selection_sort(arr):

    for i in range(0, len(arr)):
        min_num = i
        for j in range(i+1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j

        # swap the minimum index with the fisrt elements
        arr[i], arr[min_num] = arr[min_num], arr[i]

arr = []

msg = int(input("how many input you want to take: "))

for i in range(0,msg):
    ui = int(input())
    arr.append(ui)

selection_sort(arr)
print("sorted list: ", arr)
