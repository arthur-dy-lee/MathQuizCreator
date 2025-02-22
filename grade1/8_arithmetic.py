import random

from tool.output_formatter import OutputFormatter


class ArithmeticExerciseGenerator:
    # 100以内的加减法题目生成器， 支持加数和减数是否是个位数的配置，支持是否只成成加法、减法，混合运算，最终结果和被减数始终在100以内
    def __init__(self,
                 total=500,
                 per_line=4,
                 operator_type='mixed',
                 a_is_single=False,
                 b_is_single=True,
                 formatter=OutputFormatter()):
        self.total = total
        self.per_line = per_line
        self.operator_type = operator_type
        self.a_is_single = a_is_single
        self.b_is_single = b_is_single
        self.formatter = formatter

    def _check_carry(self, a, b):
        """检查个位相加是否进位"""
        return (a % 10) + (b % 10) >= 10

    def _check_borrow(self, a, b):
        """检查个位相减是否退位"""
        return (a % 10) < (b % 10)

    def _generate_operands(self, operator):
        """生成符合要求的运算数"""
        while True:
            # 生成a的取值范围
            if self.a_is_single:
                a = random.randint(1, 9)
            else:
                a = random.randint(21, 99) if operator == '-' else random.randint(1, 99)

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
        """生成符合所有条件的算式"""
        while True:
            operator = random.choice(['+', '-']) if self.operator_type == 'mixed' else self.operator_type
            a, b = self._generate_operands(operator)

            # 验证进位/退位条件
            if operator == '+' and not self._check_carry(a, b):
                continue
            if operator == '-' and not self._check_borrow(a, b):
                continue

            return f"{a} {operator} {b} ="

    def generate(self):
        """生成题目列表"""
        return [self._generate_expression() for _ in range(self.total)]

    def format_output(self, problems):
        """格式化输出为每行指定数量题目"""
        return [f"({i//self.per_line + 1})  {'      '.join(problems[i:i+self.per_line])}"
                for i in range(0, self.total, self.per_line)]

def main():
    # 示例用法：生成a为任意位数，b为两位数的加减混合题
    generator = ArithmeticExerciseGenerator(
        operator_type='+',  # +, -, mixed
        a_is_single=False,
        b_is_single=True
    )
    problems = generator.generate()
    for line in generator.format_output(problems):
        print(line)

if __name__ == "__main__":
    main()
