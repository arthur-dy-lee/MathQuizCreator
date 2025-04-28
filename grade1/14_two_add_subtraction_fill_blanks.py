import random


class VariablePositionGenerator:
    """支持三种变量位置的非负加减法生成器（结果≤100）"""

    def __init__(self, total=100, per_line=4, line_num_start=1):
        self.total = total
        self.per_line = per_line
        self.line_num_start = line_num_start

    def _safe_randint(self, low, high):
        """安全生成随机整数（网页1解决方案）"""
        return random.randint(low, high) if low <= high else low

    def _generate_type1(self):
        """生成 a ± b = ____ 题型"""
        while True:
            a = random.randint(10, 99)  # 上限改为99避免a=100导致错误（网页4案例）
            operator = random.choice(['+', '-'])

            if operator == '-':
                b = self._safe_randint(1, a - 1)  # 确保a > b
                equation = f"{a} - {b} = __"
            else:
                # 加法时确保a + b ≤ 100（网页6范围控制逻辑）
                max_b = 100 - a
                if max_b < 1: continue  # 跳过无效范围
                b = random.randint(1, max_b)
                equation = f"{a} + {b} = __"
            return equation

    def _generate_type2(self):
        """生成 a ± ____ = b 题型"""
        while True:
            a = random.randint(10, 99)
            operator = random.choice(['+', '-'])

            if operator == '-':
                # 确保b ≤ a（网页7减法规则）
                b = random.randint(1, a - 1)
                missing = a - b
                equation = f"{a} - __ = {b}"
            else:
                # 加法时确保总和≤100（网页2范围校验）
                max_sum = 100 - a
                if max_sum < 1: continue
                sum_total = random.randint(a + 1, 100)
                missing = sum_total - a
                equation = f"{a} + __ = {sum_total}"
            return equation

    def _generate_type3(self):
        """生成 ____ ± b = c 题型"""
        while True:
            operator = random.choice(['+', '-'])
            b = random.randint(1, 99)

            if operator == '-':
                # 被减数 = c + b ≤ 100（网页3范围调整）
                max_c = 100 - b
                c = random.randint(0, max_c)
                missing = c + b
                equation = f"__ - {b} = {c}"
            else:
                # 加数 = c - b ≥ 0（网页5非负约束）
                max_c = 100 - b
                c = random.randint(b, 100)
                missing = c - b
                if missing < 0: continue
                equation = f"__ + {b} = {c}"
            return equation

    def generate(self):
        """批量生成题目（网页8异常处理增强版）"""
        problems = []
        type_funcs = [self._generate_type1, self._generate_type2, self._generate_type3]

        while len(problems) < self.total:
            try:
                problem = random.choice(type_funcs)()
                problems.append(problem)
            except ValueError as e:
                print(f"跳过无效参数组合：{str(e)}")
                continue
        return self._format(problems)

    def _format(self, problems):
        """格式化输出（每行对齐优化）"""
        chunked = [problems[i:i + self.per_line]
                   for i in range(0, len(problems), self.per_line)]
        return [
            f"({line_num:2})  " + " ".join(f"{eq:16}" for eq in line_problems)
            for line_num, line_problems in enumerate(chunked, self.line_num_start)
        ]


# 使用示例
if __name__ == "__main__":
    generator = VariablePositionGenerator(total=2200, per_line=4)
    problems = generator.generate()

    print("生成的非负加减法练习题：\n" + "=" * 50)
    for line in problems:
        print(line)