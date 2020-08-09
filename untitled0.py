# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 16:02
# @Author  : AWAYASAWAY
# @File    : 最小路径和.py
# @IDE     : PyCharm



class Solution:
    def minPathSum(self, grid: [[int]]) -> int:  # 函数返回值是 int 类型
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        print(grid[-1][-1])
        return grid[-1][-1]




if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    Solution.minPathSum(grid)
