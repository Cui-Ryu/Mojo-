# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:47:57 2017

@author: 燃烧杯
"""

import numpy as np
import matplotlib.pyplot as plt

#在这里设置迭代停止条件，要多尝试一些不同数值，最好设置大一点
MAXCOUNT = 100

#数据在这里输入，依次键入每个城市的坐标
cities = np.array([ [ 565,575 ],[ 25,185 ],[ 345,750 ],[ 945,685 ],[ 845,655 ],
[ 880,660 ],[ 25,230 ],[ 525,1000 ],[ 580,1175 ],[ 650,1130 ],[ 1605,620 ],
[ 1220,580 ],[ 1465,200 ],[ 1530,5 ],[ 845,680 ],[ 725,370 ],[ 145,665 ],
[ 415,635 ],[ 510,875 ],[ 560,365 ],[ 300,465 ],[ 520,585 ],[ 480,415 ],
[ 835,625 ],[ 975,580 ],[ 1215,245 ],[ 1320,315 ],[ 1250,400 ],[ 660,180 ],
[ 410,250 ],[ 420,555 ],[ 575,665 ],[ 1150,1160 ],[ 700,580 ],[ 685,595 ],
[ 685,610 ],[ 770,610 ],[ 795,645 ],[ 720,635 ],[ 760,650 ],[ 475,960 ],
[ 95,260 ],[ 875,920 ],[ 700,500 ],[ 555,815 ],[ 830,485 ],[ 1170,65 ],
[ 830,610 ],[ 605,625 ],[ 595,360 ],[ 1340,725 ],[ 1740,245 ] ])

def calDist(xindex, yindex):
    return (np.sum(np.power(cities[xindex] - cities[yindex], 2))) ** 0.5

def calPathDist(indexList):
    sum = 0.0
    for i in range(1, len(indexList)):
        sum += calDist(indexList[i], indexList[i - 1])
    return sum    

#path1长度比path2短则返回true
def pathCompare(path1, path2):
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False
    
def generateRandomPath(bestPath):
    a = np.random.randint(len(bestPath))
    while True:
        b = np.random.randint(len(bestPath))
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a+1]
    else:
        return a, b, bestPath[a:b+1]
    
def reversePath(path):
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath
    
def updateBestPath(bestPath):
    count = 0
    while count < MAXCOUNT:
        print(calPathDist(bestPath))
        print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        if pathCompare(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath
    
    
def draw(bestPath):
    ax = plt.subplot(111, aspect='equal')
    ax.plot(cities[:, 0], cities[:, 1], 'x', color='blue')
    for i,city in enumerate(cities):
        ax.text(city[0], city[1], str(i))
    ax.plot(cities[bestPath, 0], cities[bestPath, 1], color='red')
    plt.savefig('beilin52.png',dpi=300)
    
    plt.show()
    
def opt2():
    #随便选择一条可行路径
    bestPath = np.arange(0, len(cities))
    bestPath = np.append(bestPath, 0)
    bestPath = updateBestPath(bestPath)
    draw(bestPath)
    
opt2()

