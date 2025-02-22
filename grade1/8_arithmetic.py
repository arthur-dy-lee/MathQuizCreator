import random

from tool.output_formatter import OutputFormatter


class ArithmeticExerciseGenerator:
    """算术题生成器（保持原逻辑）"""

    def __init__(self,
                 total=50,
                 operator_type='mixed',
                 a_is_single=False,
                 b_is_single=True,
                 formatter=OutputFormatter()):
        self.total = total
        self.operator_type = operator_type
        self.a_is_single = a_is_single
        self.b_is_single = b_is_single
        self.formatter = formatter

    def _format_operand(self, num):
        """运算数标准化为两位数"""
        return f"{num:>2}"

    def _check_carry(self, a, b):
        """进位检测逻辑"""
        return (a % 10) + (b % 10) >= 10

    def _check_borrow(self, a, b):
        """退位检测逻辑"""
        return (a % 10) < (b % 10)

    def _generate_operands(self, operator):
        """生成运算数核心逻辑"""
        while True:
            # 生成a的取值范围
            a = random.randint(1, 9) if self.a_is_single else (
                random.randint(21, 99) if operator == '-' else random.randint(1, 99)
            )

            # 生成b的取值范围
            if self.b_is_single:
                b = random.randint(1, 9)
            else:
                max_b = min(a, 99) if operator == '-' else min(100 - a, 99)
                b = random.randint(1, max_b) if max_b > 0 else 1

            # 验证基础条件
            if operator == '+' and (a + b > 100):
                continue
            if operator == '-' and a < b:
                continue
            return a, b

    def _generate_expression(self):
        """生成单道题目"""
        while True:
            operator = random.choice(['+', '-']) if self.operator_type == 'mixed' else self.operator_type
            a, b = self._generate_operands(operator)

            # 验证进位/退位条件
            if operator == '+' and not self._check_carry(a, b):
                continue
            if operator == '-' and not self._check_borrow(a, b):
                continue

            # 格式化为标准算式
            return f"{self._format_operand(a)} {operator} {self._format_operand(b)} ="

    def generate(self):
        """生成并格式化题目"""
        problems = [self._generate_expression() for _ in range(self.total)]
        return self.formatter.format_output(problems)


# 使用示例
if __name__ == "__main__":
    # 创建专业排版器
    math_formatter = OutputFormatter(
        per_line=4,
        line_num_format="({:0>2d})",
        column_width=14,
        line_num_start=1
    )

    # 初始化生成器
    generator = ArithmeticExerciseGenerator(
        total=500,
        operator_type='+', # 'mixed', '+', '-'
        a_is_single=False,
        b_is_single=True,
        formatter=math_formatter
    )

    # 生成并打印
    for problem in generator.generate():
        print(problem)