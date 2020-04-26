# 算法训练营的第二周 学习笔记

# 问题
为什么先列出问题呢，是因为我发现第二周还是有很多思想不是很理解
- 树的递归
- 链表的递归

# 哈希表、映射和集合
- 哈希表多用于通过index来记录已经访问过的元素
- 哈希函数通过映射来存储数据的位置，如果哈希函数设置的不好，很有可能会发生哈希碰撞现象，一般引用链表来解决位置的冲突。  
但是用了链表又会使查询效率下降，时间复杂度退化成 O(n)。

# 树、二叉树和二叉搜索树
- 树的定义
    ````python
      class TreeNode:
          def __init__(self, val):
              self.val = val
              self.left, self.right = None, None
    ````
- linked list 是特殊化的 tree；tree 是特殊化的 graph
- 二叉树的遍历
    ```text
    前序 pre-order：    根-左-右
    中序 in-order：     左-根-右
    后序 post-order：   左-右-根
    ```
- 二叉搜索树 binary search tree
    ```text
    1. 空树也是二叉搜索树
    2. 左子树 < 根
    3. 根 < 右子树
    4. 查询、插入和删除 -- 时间复杂度为O(logN)
    5. 如果 BST 全都只有左或者右节点，退化成链表，时间复杂度也退化为O(n)
    ```

# 堆 heap
- 堆的根节点只有最大值或者最小值，二者取其一
- 例如大顶堆
    ```text
    find max: O(1)
    delete max: O(logN)
    insert(create): O(logN) or O(1)-斐波拉契堆
    ```
- 二叉堆






# 图
- Graph(V,E)
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

