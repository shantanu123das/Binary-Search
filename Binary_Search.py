
def Binarysearch(arr,target):
    s=0
    e=len(arr)-1
    #checking the arry is sorted in ascending order or not
    isAsc=(arr[s]<arr[e])
    
    while(s<=e):
            mid=s+(e-s)//2
            if (arr[mid]==target):
                return mid
            if(isAsc):
                if (arr[mid]>target):
                  e=mid-1
                else:
                  s=mid+1
            else:
                if (arr[mid]<target):
                  e=mid-1
                else:
                  s=mid+1

                 
               
            
    return -1    
arr=[10,20,30,40,45,48,50]
target=30
x=Binarysearch(arr,target) 
print(x)
   