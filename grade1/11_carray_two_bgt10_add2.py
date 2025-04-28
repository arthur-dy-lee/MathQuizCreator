# -*- coding: utf-8 -*-
# @Time   : 28/4/2025 下午5:17
# @Author : arthur.dy.lee
# @Email  : arthur.dy.lee@gmail.com
# @File   : 11_carray_two_bgt10_add.py
# @Project: MathQuizCreator
import random


class AdvancedArithmeticGenerator:
    """增强版进位控制加法生成器"""

    def __init__(self,
                 total=500,
                 carry_required='mix',
                 carry_ratio=70,
                 per_line=4,
                 line_num_start=1):
        """
        :param total: 总题目数
        :param carry_required: 进位模式(carry/no_carry/mix)
        :param carry_ratio: 混合模式下的进位题占比(0-100)
        :param per_line: 每行题目数
        :param line_num_start: 起始行号
        """
        self.total = total
        self.carry_mode = carry_required
        self.carry_ratio = carry_ratio / 100  # 转换为比例
        self.per_line = per_line
        self.line_num_start = line_num_start

    def _generate_valid_pair(self):
        """生成符合当前模式的运算数对"""
        while True:
            a = random.randint(10, 99)
            b_max = 100 - a

            if b_max < 10:
                continue
            b = random.randint(10, b_max)

            a_units = a % 10
            b_units = b % 10
            sum_units = a_units + b_units

            # 动态判断进位需求
            if self.carry_mode == 'mix':
                require_carry = random.random() < self.carry_ratio
            else:
                require_carry = self.carry_mode == 'carry'

            # 进位条件判断
            is_carry = sum_units >= 10
            if require_carry and not is_carry:
                continue
            if not require_carry and is_carry:
                continue

            return a, b, is_carry  # 返回实际进位状态

    def _batch_generate(self):
        """批量生成题目并记录进位状态"""
        exercises = []
        carry_count = 0
        while len(exercises) < self.total:
            a, b, is_carry = self._generate_valid_pair()
            exercises.append((f"{a:>2} + {b:>2} =__", is_carry))
            if is_carry:
                carry_count += 1
        return exercises, carry_count

    def _format_lines(self, problems):
        """带进位标注的格式化输出"""
        chunked = [problems[i:i + self.per_line]
                   for i in range(0, len(problems), self.per_line)]
        formatted = []
        for line_num, line_problems in enumerate(chunked, self.line_num_start):
            line_str = f"({line_num})  " + "    ".join([p[0] for p in line_problems])
            formatted.append(line_str)
        return formatted

    def generate(self):
        """生成最终题目并返回统计信息"""
        problems, carry_count = self._batch_generate()
        output = self._format_lines(problems)

        # 生成统计报告
        stats = {
            "total": self.total,
            "carry_percent": round(carry_count / self.total * 100, 1),
            "non_carry_percent": round(100 - carry_count / self.total * 100, 1)
        }
        return output, stats


# 使用示例
if __name__ == "__main__":
    generator = AdvancedArithmeticGenerator(
        total=1000,
        carry_required='mix',
        carry_ratio=80,
        per_line=4,
        line_num_start=1
    )

    problems, stats = generator.generate()

    # 打印题目
    for line in problems:
        print(line)

    # 打印统计
    print(f"\n统计报告：进位题占比 {stats['carry_percent']}%，非进位题占比 {stats['non_carry_percent']}%")