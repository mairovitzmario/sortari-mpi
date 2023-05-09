#INSERTION SORT
def insertion_sort(a):
    cnt = 0
    for i in range(1, len(a)):
        aux = a[i]
        j=i-1
        cnt+=1
        ok = False
        while j>=0 and aux < a[j]:
            a[j+1]=a[j]
            j=j-1
            if ok==False:
                cnt-=1
                ok = True
            cnt+=1
        a[j+1]=aux
    return cnt


#SELECTION SORT
def selection_sort(a):
    cnt = 0
    for i in range(len(a)-1):
        k=i
        for j in range(i+1,len(a)):
            cnt+=1
            if a[k]>a[j]:
                k=j
        if k>i:
            a[k],a[i]=a[i],a[k]
    return cnt


#BUBBLE SORT
def bubble_sort(a):
    cnt = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            cnt+=1
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                sorted = False
    return cnt


#MERGE SORT
cntmerge = 0
def mergeSort(arr):
    global cntmerge
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            cntmerge+=1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            cntmerge+=1
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            cntmerge+=1
            arr[k] = R[j]
            j += 1
            k += 1

def merge_sort(lst):
    global cntmerge
    cntmerge = 0
    mergeSort(lst)
    return cntmerge


#QUICK SORT
cntquick = 0
import random
 

def quicksort(arr, start , stop):
    if(start < stop):
        pivotindex = partitionrand(arr,\
                             start, stop)
         
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
 
def partitionrand(arr , start, stop):
 
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
 
def partition(arr,start,stop):
    pivot = start # pivot
    global cntquick

    i = start + 1
     
    for j in range(start + 1, stop + 1):
        cntquick+=1
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

def quick_sort(lst):
    global cntquick
    cntquick = 0
    quicksort(lst,0,len(lst)-1)
    return cntquick


#COUNTING SORT
def counting_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    cnt = len(arr)
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    for i in range(0, len(arr)):
        cnt+=1
        count_arr[arr[i]-min_element] += 1
 

    for i in range(1, len(count_arr)):
        cnt+=1
        count_arr[i] += count_arr[i-1]
 

    for i in range(len(arr)-1, -1, -1):
        cnt+=1
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    for i in range(0, len(arr)):
        cnt+=1
        arr[i] = output_arr[i]
    
    return cnt


#RADIX SORT
def countingSort(arr, exp1):
    cnt = 0
    n = len(arr)
 
    output = [0] * (n)
 
    count = [0] * (10)
  
    for i in range(0, n):
        cnt+=1
        index = arr[i] // exp1
        count[index % 10] += 1
 

    for i in range(1, 10):
        cnt+=1
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        cnt+=1
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    i = 0
    for i in range(0, len(arr)):
        cnt+=1
        arr[i] = output[i]
    return cnt
 

def radix_sort(arr):
    cnt=0

    max1 = max(arr)
 
    exp = 1
    while max1 / exp >= 1:
        cnt+=countingSort(arr, exp)
        exp *= 10
    return cnt


#SHELL SORT
def shell_sort(arr):
    n = len(arr)
    cnt=0
    # code here
    gap=n//2
      
      
    while gap>0:
        j=gap

        while j<n:
            i=j-gap 
              
            while i>=0:
                cnt+=1
                if arr[i+gap]>arr[i]:
  
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
  
                i=i-gap 
                            
            j+=1
        gap=gap//2
    return cnt


#SHAKER SORT
def shaker_sort(a):
    cnt=0
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            cnt+=1
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if (swapped == False):
            break
 

        swapped = False

        end = end-1
        for i in range(end-1, start-1, -1):
            cnt+=1
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
 
        start = start + 1
    return cnt


#TIM SORT
MIN_MERGE = 32
cnttim = 0 
 
def calcMinRun(n):

    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 

def insertionSort(arr, left, right):
    global cnttim
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            cnttim+=1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 

def merge(arr, l, m, r):
    global cnttim
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
 
    while i < len1 and j < len2:
        cnttim+=1
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    while i < len1:
        cnttim+=1
        arr[k] = left[i]
        k += 1
        i += 1
 
    while j < len2:
        cnttim+=1
        arr[k] = right[j]
        k += 1
        j += 1
 

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 
    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 

            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size

def tim_sort(lst):
    global cnttim
    cnttim=0
    timSort(lst)
    return cnttim

if __name__ == "__main__":
    from list_generator import *

    lst = generate_list(100,0,100000)
    print(insertion_sort(lst))
    lst = generate_list(1000,0,100000)
    