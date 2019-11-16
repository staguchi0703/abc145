# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
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
import itertools
import math

num = int(input())
town_list = [[int(item) for item in input().split()] for _ in range(num)]

root_list = list(itertools.permutations(list(range(num))))

length = 0

for root in root_list:
    for i in range(num-1):
        temp_path = root[i:i+2]
        first = temp_path[0]
        second = temp_path[1]

        x_length = town_list[first][0] - town_list[second][0]
        y_length = town_list[first][1] - town_list[second][1]


        length += math.sqrt(x_length**2 + y_length**2)
print(length / len(root_list))



