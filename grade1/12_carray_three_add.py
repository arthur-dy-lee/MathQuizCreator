import random
import re


class TripleDigitArithmeticGenerator:
    """三位数加法生成器（支持进位比例控制）"""

    def __init__(self,
                 total=500,
                 carry_ratio=80,
                 per_line=4,
                 line_num_start=1):
        """
        :param total: 总题目数
        :param carry_ratio: 个位进位比例(0-100)
        :param per_line: 每行题目数
        :param line_num_start: 起始行号
        """
        self.total = total
        self.carry_ratio = carry_ratio / 100
        self.per_line = per_line
        self.line_num_start = line_num_start

    def _generate_valid_triple(self):
        """生成符合条件的三位数组合"""
        while True:
            # 生成两个两位数（确保至少两个两位数）
            a = random.randint(10, 70)
            b = random.randint(10, min(80 - a, 99))
            remaining = 100 - a - b

            # 第三个数取值范围控制
            c_min = 1 if (a >= 10 and b >= 10) else 10  # 确保至少两个两位数
            c = random.randint(c_min, min(remaining, 99))

            # 个位进位检测
            units_sum = (a % 10) + (b % 10) + (c % 10)
            is_carry = units_sum >= 10

            # 动态调整进位概率
            require_carry = random.random() < self.carry_ratio
            if require_carry != is_carry:
                continue

            # 最终结果验证
            if a + b + c > 100:
                continue

            return a, b, c

    def _batch_generate(self):
        """批量生成题目"""
        exercises = []
        carry_count = 0
        while len(exercises) < self.total:
            a, b, c = self._generate_valid_triple()
            units_sum = (a % 10) + (b % 10) + (c % 10)
            is_carry = units_sum >= 10
            exercises.append(f"{a:>2} + {b:>2} + {c:>2} =____")
            if is_carry:
                carry_count += 1
        return exercises, carry_count

    def _format_lines(self, problems):
        """格式化输出"""
        chunked = [problems[i:i + self.per_line]
                   for i in range(0, len(problems), self.per_line)]
        return [
            f"({line_num})  " + "    ".join(line_problems)
            for line_num, line_problems in enumerate(chunked, self.line_num_start)
        ]

    def generate(self):
        """生成并返回统计信息"""
        problems, carry_count = self._batch_generate()
        output = self._format_lines(problems)

        stats = {
            "total": self.total,
            "carry_percent": round(carry_count / self.total * 100, 1),
            "avg_sum": round(sum(
                # 使用正则表达式提取所有数字
                sum(map(int, re.findall(r'\d+', problem.split('=')[0])))
                for line in output
                for problem in line.split('   ')
            ) / self.total, 1)
        }
        return output, stats


# 使用示例
if __name__ == "__main__":
    generator = TripleDigitArithmeticGenerator(
        total=2000,
        carry_ratio=70,
        per_line=3,
        line_num_start=100
    )

    problems, stats = generator.generate()

    # 打印题目
    for line in problems:
        print(line)

    # 打印统计
    print(f"\n统计报告：平均和值 {stats['avg_sum']}，实际进位比例 {stats['carry_percent']}%")