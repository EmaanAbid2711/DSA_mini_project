import math
def filter_num(value, colName):
    
    if isinstance(value, (int, float)):
        return float(value) 
    if(colName==1):
        try:
            filtered_val = float(value.replace('Rs.', '').replace(',', '').strip())
        except ValueError:
            filtered_val = 0.0 # when value cannot convert
        return filtered_val
    
    
    elif (colName==2):
        try:
            if (value=='No discount'):
                filtered_val = 0
            else:
                filtered_val = float(value.replace('%', '').replace('Off', '').strip())
        except ValueError:
            filtered_val = 0.0 
        return filtered_val
    elif (colName==3):
        
        filtered_val = value.replace('sold', '').strip()
        try:
            if filtered_val.endswith('K'):
                filtered_val = float(filtered_val[:-1]) * 1000  
            else:
                filtered_val = float(filtered_val)
        except ValueError:
            filtered_val = 0.0
        filtered_val = math.floor(filtered_val)
        return filtered_val
    elif (colName==4):
        
        filtered_val = value.replace('sold', '').strip()
        try:
            if filtered_val.endswith('K'):
                filtered_val = float(filtered_val[:-1]) * 1000  
            else:
                filtered_val = float(filtered_val)
        except ValueError:
            filtered_val = 0.0
        filtered_val = math.floor(filtered_val)
        return filtered_val
    
    else:
        return value
    
# bubble sort
def BubbleSort(arr, colName) :
    flag = True
    i = 0
    n = len(arr)
    while flag :
        flag = False
        for j in range(n-i-1):
            if filter_num(arr[j][colName],colName) > filter_num(arr[j+1][colName],colName):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        i +=1
    return arr

#Selection Sort
def SelectionSort(arr, colName):
    n = len(arr)
    for i in range (0, n-1):
        min_idx = i
        for j in range (i+1, n):
            if filter_num(arr[j][colName],colName) < filter_num(arr[min_idx][colName],colName):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Insertion Sort
def InsertionSort(arr, colName):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and filter_num(arr[j][colName],colName) > filter_num(key[colName],colName) :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Merge Sort
def MergeSort(arr, colName):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid] 
        right = arr[mid:]
        MergeSort(left, colName)
        MergeSort(right, colName)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if filter_num(left[i][colName],colName) < filter_num(right[j][colName],colName):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1   
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

#Quick sort
def QuickSort (arr, colName):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = arr[n // 2]
        middle = [x for x in arr if filter_num(x[colName],colName) == filter_num(pivot[colName],colName)]
        right = [x for x in arr if filter_num(x[colName],colName) > filter_num(pivot[colName],colName)]
        left = [x for x in arr if filter_num(x[colName],colName) < filter_num(pivot[colName],colName)]

        return QuickSort (left,colName) + middle + QuickSort(right,colName)

#Counting Sort
def CountingSort(arr, colName):
    
    filtered_val = [filter_num(item[colName], colName) for item in arr]
    Min = min(filtered_val)
    Max = max(filtered_val)
    n = len(arr)
    
    range_val = int(Max - Min + 1)
   
    countArray = [0] * range_val
    output = [0] * n

    for value in arr:
        idx = int(filter_num(value[colName],colName))-int(Min)
        countArray[idx] += 1

    m = len(countArray)
    for i in range(1, m):
        countArray[i] += countArray[i - 1]

    for value in reversed(arr): 
        idx = int (filter_num(value[colName],colName))-int(Min)
        output[countArray[idx] - 1] = value 
        countArray[idx] -= 1

    for i in range(n):
        arr[i] = output[i]

    return arr

# Radix sort
def RadixSort(arr,colName):
    
    Max = int(max(filter_num(row[colName], colName) for row in arr))
    exp = 1
    while Max // exp > 0:
        RadixCount(arr, exp,  colName)
        exp *= 10
        
    return arr

def RadixCount(arr, exp, colName):
    
    n = len(arr)
    output = [0] * n
    count = [0] * 20

    for i in range(n):
        idx = int(filter_num(arr[i][colName],colName)) // exp
        count[idx%10+10] += 1

    m = len(count)
    for i in range(1, m):
        count[i] += count[i - 1]

    for i in range(n-1, -1, -1):
        idx = int (filter_num(arr[i][colName],colName)) // exp
        output[count[idx % 10+10] - 1] = arr[i]
        count[idx % 10+10] -= 1

    for i in range(n):
        arr[i] = output[i]

# Bucket Sort
import math

def BucketSort(arr, colName):
    
    filtered_val =  [filter_num(row[colName],colName) for row in arr]
    Min = int(min(filtered_val))
    Max = int(max(filtered_val))
    n =int(len(arr))
    range_val = Max - Min
    buckets = [[] for _ in range(n)]
    
    for row in arr:
        Value = (filter_num(row[colName],colName) - Min)/(range_val + 1)
        idx = math.floor(Value * n)
        buckets[idx].append(row)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket, key=lambda x: filter_num(x[colName], colName)))
    
    return sorted_arr





