# -*- coding: utf-8 -*-
# @Time   : 5/9/2025 19:27
# @Author : arthur.dy.lee
# @Email  : arthur.dy.lee@gmail.com
# @File   : 4_MathProblemGenerator.py
# @Project: MathQuizCreator


import random

"""
帮我生成python加减法算法，要求：0，起一个类名和main测试，1. 计算结果不超过100，不允许有负数出现。
2. 帮我出以下类型的题目， 7+__ = 30+2, 31-3=__ - 6

3. 结果要在最后总一打印，要带题目数字标号，和题目一一对应。  4. 其它参数：参数:
num_problems -- 生成总题目数量
lines_per_problem -- 每题后的空行数 (默认1)
problems_per_line -- 每行题目数 (默认2)，
每个题都带有数字标号。
输出的题目结果要对齐。最后的结果即等号右边带2个下划线。
"""

class MathProblemGenerator:
    def __init__(self, num_problems, lines_per_problem=1, problems_per_line=2):
        self.num_problems = num_problems
        self.lines_per_problem = lines_per_problem
        self.problems_per_line = problems_per_line
        self.problems = []
        self.answers = []

    def generate_problem(self):
        problem_type = random.choice(['A', 'B'])

        if problem_type == 'A':  # 类型：7+__ = 30+2
            # 生成右侧完整表达式
            while True:
                right_num1 = random.randint(10, 98)
                right_num2 = random.randint(1, min(10, 100 - right_num1))
                right_result = right_num1 + right_num2
                if right_result <= 100:
                    break

            # 生成左侧已知部分
            left_num = random.randint(1, min(50, right_result))
            blank_value = right_result - left_num

            problem_str = f"{left_num} + __ = {right_num1} + {right_num2}"
            return problem_str, blank_value

        else:  # 类型：31-3=__ - 6
            # 生成左侧完整表达式
            while True:
                left_num1 = random.randint(20, 100)
                left_num2 = random.randint(1, min(19, left_num1))
                left_result = left_num1 - left_num2
                if left_result >= 0:
                    break

            # 生成右侧已知部分
            right_num = random.randint(1, min(10, 100 - left_result))
            blank_value = left_result + right_num

            problem_str = f"{left_num1} - {left_num2} = __ - {right_num}"
            return problem_str, blank_value

    def generate_all(self):
        for i in range(self.num_problems):
            problem, answer = self.generate_problem()
            self.problems.append(problem)
            self.answers.append(answer)

    def display(self):
        # 计算最大宽度用于对齐
        max_width = max(len(prob) for prob in self.problems) + 10

        # 打印题目
        for i, problem in enumerate(self.problems, 1):
            # 添加题目编号
            formatted_problem = f"{i}. {problem}"

            # 对齐处理
            formatted_problem = formatted_problem.ljust(max_width)

            # 换行处理
            end_char = '\n' * self.lines_per_problem if i % self.problems_per_line == 0 else ''
            print(formatted_problem, end=end_char)

        # 打印答案
        print("\n\n答案：")
        for i, answer in enumerate(self.answers, 1):
            print(f"{i}. {answer}")


if __name__ == "__main__":
    # 创建生成器实例
    generator = MathProblemGenerator(
        num_problems=600,  # 生成10个题目
        lines_per_problem=1,  # 每题后空1行
        problems_per_line=3  # 每行显示2个题目
    )

    # 生成并显示题目
    generator.generate_all()
    generator.display()