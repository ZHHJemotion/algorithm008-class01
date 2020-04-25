# 算法训练营的第二周 学习笔记

# 问题
为什么先列出问题呢，是因为我发现第二周还是有很多思想不是很理解
- 树的递归
- 链表的递归
- 





# 图

- 图的常见算法
1. DFS的递归写法模版
    ```python
   visited = set()  # 和树中的DFS的最大区别，因为树无环路，而图有环路
   def DFS(node, visited):
       if node in visited:  # terminator
           # already visited
           return 
       
       visited.add(node)
       # process current node here
       ...
       for next_node in node.children():
           if next_node not in visited:
               DFS(next_node, visited)
    ```
2. BFS的模版
    ```python
   def BFS(graph, start, end):
       queue = []
       queue.append([start])
       visited = set()  # 和树中的DFS的最大区别，因为树无环路，而图有环路
       while queue:
           node = queue.pop()
           visited.add(node)
           process(node)
           nodes = generated_related_nodes(node)
           queue.push(nodes)
    ```

