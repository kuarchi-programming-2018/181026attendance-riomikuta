# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:47:39 2018

@author: 石坂 梨緒
"""

def grow(s, r):  # 文字列sと繰り返し回数rを入力
    ss = ''  # 出力する文字列を初期化
    for i in s:#文字列を一文字ずつ取り出してループする
        if i=='f':
            ss+='fg'  # ' f'  を ' fg'  に書き換え
        elif i=='g':
            ss+='gh'  # ' g'  を ' gh'  に書き換え
        elif i=='h':
            ss+='gf'  # hをgfに書き換え
        else:
            ss+=i
    r=r-1    # 残りの繰返し回数を1減らす
    print(ss)
    if r>0:
       ss=grow(ss,r)
    # 繰返し回数が0でない時，自分自身を呼び出す
        

grow('fXgXh', 4)  # growを2回実行





