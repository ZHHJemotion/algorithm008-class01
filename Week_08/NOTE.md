# 算法训练营的第八周 学习笔记

# 初级排序
## 选择排序
### python 代码
```python
def selection_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
```

## 插入排序
### python 代码
```python
def insertion_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if nums[i] < nums[j-1]:
                    nums[i], nums[j-1] = nums[j-1], nums[i]
                else:
                    break
        return nums
```

## 冒泡排序
### python 代码
```python
def bubble_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[i] > nums[j+1]:
                    nums[i], nums[j+1] = nums[j+1], nums[i]
        return nums    
```

# 高级排序
## 快速排序
### python 代码
```python
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)

def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```

## 归并排序
### python 代码
```python
def merge_sort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```

## 堆排序
### python 代码
```python
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heap_sort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```