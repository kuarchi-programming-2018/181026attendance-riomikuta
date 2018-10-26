# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:23:46 2018

@author: 石坂 梨緒
"""


import turtle as tl


def draw(length, depth):
    if depth==0:
        tl.fd(length)
    else:
        draw(length/3, depth-1)
        tl.lt(60)
        draw(length/3, depth-1)
        tl.rt(120)
        draw(length/3, depth-1)
        tl.lt(60)
        draw(length/3, depth-1)
    
         # 書く
         
    
    
# tl.tracer(0,0) # no animation
tl.up()
tl.setx(-250)
tl.down()
# tl.speed(0)  # 0:fastest, 1:slow to 10:fast
draw(500, 3)
tl.done()