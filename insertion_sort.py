# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

number = int(input("how many number you want to input: "))
arr = input("enter the numbers: ")
l = list(map(int,arr.split(' ')))
# arr = [12, 11, 13, 5, 6]
insertionSort(arr)

print(arr)
