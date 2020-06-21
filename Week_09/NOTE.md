# 算法训练营的第九周 学习笔记

### 《不同路径2》的状态转移方程
```python
if obstacleGrid[i][j] == 0:
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
else:
    dp[i][j] = 0
```