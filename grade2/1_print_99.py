# -*- coding: utf-8 -*-
# @Time   : 28/4/2025 下午6:26
# @Author : arthur.dy.lee
# @Email  : arthur.dy.lee@gmail.com
# @File   : 1_print_99.py
# @Project: MathQuizCreator
# 进阶版（带编号对齐）
for i in range(1, 10):
    line = []
    for j in range(1, i+1):
        ret = j*i
        line.append(f"{j}×{i}={ret}")
    print(f"({i})  " + "\t".join(line))