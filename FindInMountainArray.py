class SearchInMountain:
    def search(self, arr, target):
        peak = self.peakIndexInMountainArray(arr)
        first_try = self.orderAgnosticBS(arr, target, 0, peak)
        if first_try != -1:
            return first_try
        # try to search in second half
        return self.orderAgnosticBS(arr, target, peak+1, len(arr) - 1)

    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > arr[mid+1]:
                # you are in dec part of array
                # this may be the ans, but look at left
                # this is why end != mid - 1
                end = mid
            else:
                # you are in asc part of array
                start = mid + 1  # because we know that mid+1 element > mid element
        # in the end, start == end and pointing to the largest number because of the 2 checks above
        # start and end are always trying to find max element in the above 2 checks
        # hence, when they are pointing to just one element, that is the max one because that is what the checks say
        # more elaboration: at every point of time for start and end, they have the best possible answer till that time
        # and if we are saying that only one item is remaining, hence cuz of above line that is the best possible ans
        return start  # or return end as both are =

    def orderAgnosticBS(self, arr, target, start, end):
        # find whether the array is sorted in ascending or descending
        is_asc = arr[start] < arr[end]

        while start <= end:
            # find the middle element
            mid = start + (end - start) // 2

            if arr[mid] == target:
                return mid

            if is_asc:
                if target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

arr = [1, 2, 3, 4, 5, 3, 1]
target = 3

search_obj = SearchInMountain()
result = search_obj.search(arr, target)
print(result)  # Output: 2 (index of the target value in the array)
