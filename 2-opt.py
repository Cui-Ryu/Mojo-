# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 16:50
# @Author  : AWAYASAWAY
# @File    : 2-opt.py
# @IDE     : PyCharm
'''
城市berlin52 TSP问题的最优解为 7452
step1 随机选择一条路径；
step2 设置算法停止参数countMax
step3 随机选择两个节点，将结点之间的路径翻转，若新路径更优，则迭代次数count+1，更新路径；否则置0.
step4 若迭代次数小于countMax,停止；否则，重复step3。
'''

import numpy as np
import matplotlib.pyplot as plt

# 设置停止条件
countMax = 100


def city(fname):
    '''
    :param fname: berlin52.txt
    :return: 城市坐标 [ [565.0, 575.0], ..., [] ]
    '''
    location = []  # 存储城市坐标点
    cities = [] # 存储城市坐标点
    with open(fname) as f:
        for line in f:
            if line == '\n':
                line = line.strip('\n')  # 删除文件中的空白行
            else:
                line = ((line.strip('\n')).strip('')).split((' '))  # 删除换行和首尾空白格
                location.append(line)
        for i in range(len(location)):
            x = float(location[i][1])
            y = float(location[i][2])
            cities.append([x, y])
        cities = np.array(cities)

    return cities


def dist_2city(cities):
    '''
    :param location: 城市坐标
    :return: 城市距离矩阵 distance
    '''
    n = len(cities)
    distance = [[0 for col in range(n)] for raw in range(n)]
    for i in range(n):
        for j in range(n):
            x = pow(float(cities[i][0]) - float(cities[j][0]), 2)
            y = pow(float(cities[i][1]) - float(cities[j][1]), 2)
            distance[i][j] = pow(x + y, 0.5)  # 生成城市距离矩阵
    return distance


def generatePath(bestPath):
    '''
    :param bestPath:
    :return: 生成路径
    '''
    l = len(bestPath)
    a = np.random.randint(0, l)  # 随机产生一个整数
    while True:
        b = np.random.randint(0, l)
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a + 1]
    else:
        return a, b, bestPath[a:b + 1]


def reversePath(path):
    '''
    :param path:
    :return: 翻转路径 path
    '''
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath

def calcPath(path):
    '''
    :param path:
    :return: 计算路径 path 的距离
    '''
    dist = dist_2city(cities)
    sumPath = 0.0
    l = len(path)
    for i in range(0, l-1):
        sumPath += dist[path[i]][path[i+1]]
    return sumPath

def comparePath(path1, path2):
    '''
    :param path1:
    :param path2:
    :return: 比较两条路径的长度
    '''
    if calcPath(path1) < calcPath(path2):
        return True
    else:
        return False

def updateBestPath(bestPath):
    '''
    :param bestPath:
    :return:
    '''
    count = 0
    while count < countMax:
        print(calcPath(bestPath))
        print(bestPath.tolist())
        start, end, path = generatePath(bestPath)
        rePath = reversePath(path)
        if comparePath(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath

def draw(cities, bestPath):
    '''
    :param cities:
    :param bestPath:
    :return:
    '''
    ax = plt.subplot(111, aspect='equal')
    ax.plot(cities[:, 0], cities[:, 1], 'o', color='blue')
    for i, city in enumerate(cities):
        ax.text(city[0], city[1], str(i))
    ax.plot(cities[bestPath, 0], cities[bestPath, 1], color='red')
    ax.set_title('2-opt algorithm to solve TSP')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    plt.savefig('2-opt.jpg', dpi=500)
    plt.show()


if __name__ == '__main__':
    fname = 'berlin52.txt'
    cities = city(fname)
    bestPath = np.arange(0, len(cities))
    bestPath = np.append(bestPath, 0)
    bestPath = updateBestPath((bestPath))
    draw(cities, bestPath)

