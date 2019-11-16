# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
X, Y = [int(item) for item in input().split()]

if X < Y:
    X, Y = Y, X


def judge(x, y):
    if x == 2*y:
        return y
    else: return -1

num = Y // 3 + 1
temp_root = 0
res = 0

if judge(X, Y) < 0:

    for i in range(1,num):
        X, Y = X - 3, Y - 3
        temp_root += 2**i
        if judge(X, Y) >= 0:
            res = judge(X, Y) + temp_root
            break
    print(res % (10**9 + 7))
else:
    print(judge(X, Y) % (10**9 + 7))