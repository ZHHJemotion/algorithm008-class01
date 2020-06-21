# 算法训练营的第九周 学习笔记

## 高级动态规划
```text
    定义状态 + 状态转移方程
```
复杂度来源
```text
1. 状态拥有更多的维度
2. 状态方程更加复杂
```

## 字符串算法
### 字符串的基本知识
```text
    切记：
        1. python 和 JAVA 的 string 都是 immutable，基于线程安全考虑
        2. C++ 的 string 是 mutable 的，若要使其 immutable，用 const
```
### 高级字符串算法
#### 最长字串/子序列
1. Longest Common Sequence (最长子序列)
```python
    dp[i][j] = dp[i-1][j-1] + 1 (if s1[i-1] == s2[j-1])
    else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```
2. Longest Common Substring (最长字串)
```python
    dp[i][j] = dp[i-1][j-1] + 1 (if s1[i-1] == s2[j-1])
    else dp[i][j] = 0
```
3. Edit Distance (编辑距离)
### 字符串匹配算法
1. 暴力法（brute force) -- O(mn)
以为皆是对暴力法的优化
2. Rabin-Karp算法
3. KMP 算法

### 《不同路径2》的状态转移方程
```python
if obstacleGrid[i][j] == 0:
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
else:
    dp[i][j] = 0
```