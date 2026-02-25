#remove dublicates from sorted array

arr = [5, 5, 6, 7, 7, 12, 12, 12, 34, 36, 55, 55, 56]
x = 0
print(f"Array before:", arr)
for i in range(1, len(arr)):
    if arr[i] != arr[x]:
        x += 1
        arr[x] = arr[i]
print("arr", arr)
arr = arr[:x+1]
print(arr)