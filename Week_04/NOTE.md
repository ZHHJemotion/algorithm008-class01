# 算法训练营的第四周 学习笔记

# DFS & BFS
## DFS 代码模版
- 递归
    ```python
      visited = set() 

      def dfs(node, visited):
          if node in visited: # terminator
              # already visited 
              return 
        
          visited.add(node) 
        
          # process current node here. 
          ...
          for next_node in node.children(): 
              if next_node not in visited: 
                  dfs(next_node, visited)
    ```
  
- 迭代 -- 栈
    ```python
        def DFS(self, tree): 
            if tree.root is None: 
                return [] 
                
            visited, stack = [], [tree.root]
            
            while stack: 
                node = stack.pop() 
                visited.add(node)
                process (node) 
                nodes = generate_related_nodes(node) 
                stack.push(nodes) 
     
            # other processing work 
            ...
    ```
## BFS 代码模版
- 队列
    ```python
    def BFS(graph, start, end):
        visited = set()
        queue = [] 
        queue.append([start]) 
    
        while queue: 
            node = queue.pop() 
            visited.add(node)
    
            process(node) 
            nodes = generate_related_nodes(node) 
            queue.push(nodes)
    
        # other processing work 
        ...
    ```
  
  
# 二分查找
## 代码模板
```python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```
## 153. 寻找旋转排序数组中的最小值
解题思路
```text
    step 1. 判断 nums 的长度，如果长度是1，则最小值为 nums[0]
    step 2. 判断是否为单调递增，如果最后的元素大于最左的元素，则说明单调递增，没有旋转
    step 3. 进入二分查找的 while 循环
        3.1 如果中间点大于其后面的相邻点，则这个相邻点为旋转的拐点，为最小点
        3.2 如果中间点小于其前面的相邻点，则该中间点为旋转的拐点，为最小点
        3.3 比较中间点和下标为0的元素大小
            3.3.1 如果中间点大于下标为0的元素，则下标为0的元素到中间点为递增，则判断右边的列表
            3.3.2 如果中间点小于下标为0的元素，则下标为0的元素到中间点为无序，则判断左边的列表
```

代码
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1
        # 递增没有拐点
        if nums[l] <  nums[r]:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2
            
            # 拐点
            if nums[mid] > nums[mid+1]:
                return nums[mid+1] 
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            # 判断有序性
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
```