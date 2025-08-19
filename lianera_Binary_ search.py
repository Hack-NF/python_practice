
                    #LINEAR SEARCH
def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print("target {} found at index {}".format(x,i))
            return
    return -1

                    #BINERY SEARCH
def binarysearch(arr, x):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == x:
            print(f"{x} found at index {mid}")
            return
        elif arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    return -1

    
n = (int(input("Enter the number of elements in an array: ")))
arr = []
for i in range(n):
    val = input(f"enter element at index {i}: ")
    arr.append(val)
for i in range(n):
    print("Index {} -> value {}".format(i,arr[i]))

x = (input("Enter number u want to search: "))
print("Choose search method")
print("Enter 1 for linear search: ")
print("Enter 2 for binary search: ")
choise = int(input("Enter choise(1/2): "))

if choise == 1:
    result = linearsearch(arr, x)
elif choise == 2:
    result = binarysearch(arr, x)
else:
    print("Invaild choise")    
    result = -1

if result != -1:
    print(f"{x} found at index {result}")
else:
    print("Not found")    


              

