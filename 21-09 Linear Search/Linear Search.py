def linear_search(arr,target):
    for i in range(len(arr)):
        print(i)
        if arr[i] == target:
            return i
    return -1
arr = list(map(int,input("Enter the List of values separate from space: ").split()))
target = int(input("Enter the Find value of Number: "))
result = linear_search(arr,target)
if result != -1:
    print(f" your target index value: {result}")
else:
    print("Your Target not found")