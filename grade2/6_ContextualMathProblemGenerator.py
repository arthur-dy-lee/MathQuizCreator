# -*- coding: utf-8 -*-
# @Time   : 5/9/2025 19:51
# @Author : arthur.dy.lee
# @Email  : arthur.dy.lee@gmail.com
# @File   : 6_ContextualMathProblemGenerator.py
# @Project: MathQuizCreator

import random

"""
学校教学和语文兴趣小组的人数正好相等，都是24人，现在如果要从数学小组抽出5人到语文小组，那么数学小组比语文小组少了（__）人
"""

class ContextualMathProblemGenerator:
    def __init__(self, num_problems, lines_per_problem=2):
        self.num_problems = num_problems
        self.lines_per_problem = lines_per_problem
        self.problems = []
        self.answers = []

    def generate_problems(self):
        for i in range(self.num_problems):
            # 生成初始人数（10-49之间，确保调动后不超过100）
            initial = random.randint(10, 49)
            # 生成调动人数（1-10之间，确保不会出现负数）
            transfer = random.randint(1, 10)

            # 计算答案（数学小组比语文小组少的人数）
            answer = 2 * transfer

            # 构建题目
            problem = (
                f"{i + 1}. 学校教学和语文兴趣小组的人数正好相等，都是{initial}人，"
                f"现在如果要从数学小组抽出{transfer}人到语文小组，"
                "那么数学小组比语文小组少了（__）人"
            )

            self.problems.append(problem)
            self.answers.append(answer)

    def print_problems_and_answers(self):
        # 打印所有题目
        for problem in self.problems:
            print(problem)
            for _ in range(self.lines_per_problem):
                print()

        # 打印答案
        print("\n答案：")
        for i, answer in enumerate(self.answers):
            print(f"{i + 1}. {answer}")


def main():
    # 生成10道题目，每题后空2行
    generator = ContextualMathProblemGenerator(num_problems=10, lines_per_problem=2)
    generator.generate_problems()
    generator.print_problems_and_answers()


if __name__ == "__main__":
    main()
