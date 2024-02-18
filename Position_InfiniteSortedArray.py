def ans(arr, target):
    # first find the range
    # first start with a box of size 2
    start = 0
    end = 1

    # condition for the target to lie in the range
    while target > arr[end]:
        temp = end + 1  # this is my new start
        # double the box value
        #for new end we need previous start and previous end
        # new end = previous end + sizeofbox*2
        end = end + (end - start + 1) * 2
        start = temp
    return binarySearch(arr, target, start, end)


def binarySearch(arr, target, start, end):
    while start <= end:
        # find the middle element
        mid = start + (end - start) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            # ans found
            return mid
    return -1


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
target = 10
print(ans(arr, target))
