# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:10:46 2018

@author: 石坂 梨緒
"""

from turtle import *  # 描画環境 turtle をインポート


def connect_points(points):
    up()
    setpos(points[-1][0], points[-1][1])
    down()
    for xy in points:
        setpos(xy[0], xy[1])
        


def n_polygon(n=4, x0=0, y0=0, size=100):
    angle = 360 / n
    up()
    setpos(x0, y0)
    points = []
    for i in range(n):
        forward(size)
        left(angle)
        points.append(pos())
    return points



def deviding(p0, p1, r):
    # 書く
    return


# deviding_point(点A,点B,内分比)
def deviding_point(p0, p1, ratio):
    # 書く
    return [xr, yr]



# deviding_points(多角形の４頂点，内分比)
def deviding_points(points, ratio):
    new_points = []
    points2 = points[:] #コピーを作成
    points2.append(points2[0])
    points2.pop(0)
    for p0, p1 in zip(points, points2):
        書く
    return new_points


def rose_window_recursion(points, ratio, depth):
    connect_points(points)
    new_points = deviding_points(points, ratio)
    if depth == 0:
        up()
        setpos(-200, -200)
    else:
        rose_window_recursion(new_points, ratio, depth - 1)
        
        
points = n_polygon(n=5, size=200)
rose_window_recursion(points, 0.1, 40)
done()      