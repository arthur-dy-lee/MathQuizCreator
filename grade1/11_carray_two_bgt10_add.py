# -*- coding: utf-8 -*-
# @Time   : 28/4/2025 下午5:17
# @Author : arthur.dy.lee
# @Email  : arthur.dy.lee@gmail.com
# @File   : 11_carray_two_bgt10_add.py
# @Project: MathQuizCreator
import random


class AdvancedArithmeticGenerator:
    """增强版算术题生成器（支持行号递增和多题排版）"""

    def __init__(self,
                 total=500,
                 carry_required=True,
                 per_line=4,
                 line_num_start=1):
        """
        :param total: 总题目数
        :param carry_required: 是否强制进位
        :param per_line: 每行题目数
        :param line_num_start: 起始行号
        """
        self.total = total
        self.carry_required = carry_required
        self.per_line = per_line
        self.line_num_start = line_num_start

    def _generate_valid_pair(self):
        """生成符合条件的一对操作数"""
        while True:
            a = random.randint(10, 99)
            b_max = 100 - a

            # 确保b为两位数且不越界
            if b_max < 10:
                continue
            b = random.randint(10, b_max)

            # 提取个位数字
            a_units = a % 10
            b_units = b % 10

            # 进位条件判断
            is_carry = (a_units + b_units) >= 10
            if self.carry_required != is_carry:
                continue

            return a, b

    def _batch_generate(self):
        """批量生成题目"""
        exercises = []
        while len(exercises) < self.total:
            a, b = self._generate_valid_pair()
            exercises.append(f"{a:>2} + {b:>2} =__")
        return exercises

    def _format_lines(self, problems):
        """将题目按行格式化"""
        chunked = [problems[i:i + self.per_line]
                   for i in range(0, len(problems), self.per_line)]
        return [
            f"({line_num})  " + "    ".join(line_problems)
            for line_num, line_problems in enumerate(chunked, self.line_num_start)
        ]

    def generate(self):
        """生成最终排版结果"""
        problems = self._batch_generate()
        return self._format_lines(problems)


# 使用示例
if __name__ == "__main__":
    generator = AdvancedArithmeticGenerator(
        total=1500,
        carry_required=False,
        per_line=4,
        line_num_start=1
    )

    for line in generator.generate():
        print(line)