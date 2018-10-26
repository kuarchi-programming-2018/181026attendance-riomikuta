# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:50:10 2018

@author: 石坂 梨緒
"""
import csv
def read_data(file_name):
    reader = csv.reader(open(file_name, 'r'))
    X = []
    Y = []
    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))
    return X, Y  # データを返す

import matplotlib.pyplot as plt

import numpy as np

def draw_graph(x,y,title,xlabel,ylabel):
    # ここに描画するプログラムを書く。
    x=np.arange(-3,3,0.1)# グラフタイトル
    y=np.sin(x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x,y)
    plt.show()
    
file_name='data3.csv'
x,y=read_data(file_name)

draw_graph(x,y,'sin(x)','xlabel','ylabel')