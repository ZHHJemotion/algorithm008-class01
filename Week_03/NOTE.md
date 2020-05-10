# 算法训练营的第三周 学习笔记

# 递归
- 回顾
    ```text
        树的面试题解法一般都是递归
        原因：
          1. 树节点的定义是用递归的方式
          2. 重复性（自相似性）
    ```
- 递归模版
    ```python
    def recursion(level, param1, param2, ...): 
        # recursion terminator 
        if level > MAX_LEVEL: 
           process_result 
           return 
        # process logic in current level 
        process(level, data...) 
        # drill down 
        self.recursion(level + 1, p1, ...) 
        # reverse the current level status if needed
    ```
- 递归的思维要点
    ```text
      1. 不要人肉进行递归 -- 递归的最大误区
      2. 找到最近最简方法，将其拆解成可重复解决的问题
      3. 数学归纳法的思维
    ```

# 分治和回溯
分治与回溯本质上也是递归，找重复性和分解问题和最后组合每个子问题的结果
- 分治的代码模板
```python
    def divide_conquer(problem, param1, param2, ...):
        # recursion terminator
        if problem is None:
            print result
            return 
        # prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)

        # conquer subproblems
        subresult_1 = self.divide_conquer(subproblems[0]), p1, q1)
        subresult_2 = self.divide_conquer(subproblems[1]), p1, q1)
        ... 

        # process abd generate the final result
        result = process_result(subresult_1, subresult_2, ...)
        
        # revert the current level status
 ```
- 回溯
```text
    回溯是在一层中不断的尝试，然后在返回上一层的时候要消除之前的操作
```
 