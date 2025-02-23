import random


class SubtractionProblemGenerator:
    def __init__(self, num_problems=500, a_range=(11, 20), b_range=(2, 9), per_row=3, print_steps=False):
        self.num_problems = num_problems
        self.a_min, self.a_max = a_range
        self.b_min, self.b_max = b_range
        self.print_steps = print_steps
        self.per_row = per_row  # 自由设置每行题目数

    def _generate_problem(self):
        """生成题目及破十法步骤"""
        while True:
            a = random.randint(self.a_min, self.a_max)
            b = random.randint(self.b_min, self.b_max)
            if b > (a % 10):
                step1 = 10 - b
                step2 = (a - 10) + step1
                problem = f"{a} - {b} =          "

                if self.print_steps:
                    steps = [
                        f"先算: ⬜⚪⬜=⬜    ",
                        f"后算: ⬜⚪⬜=⬜    "
                    ]
                    return problem + '\n' + '\n'.join(steps)
                return problem

    def generate(self):
        """支持多题横向排列的步骤生成"""
        problems = [self._generate_problem() for _ in range(self.num_problems)]

        # 按per_row分组并添加编号
        grouped = []
        for i in range(0, len(problems), self.per_row):
            group = []
            for j, p in enumerate(problems[i:i + self.per_row]):
                number = i + j + 1
                lines = p.split('\n')
                lines[0] = f"({number}) {lines[0]}"  # 添加题号到首行
                group.append(lines)
            grouped.append(group)

        # 构建横向排列的输出
        output = []
        for group in grouped:
            max_lines = max(len(p) for p in group)
            for line_idx in range(max_lines):
                line_segments = []
                for problem_lines in group:
                    if line_idx < len(problem_lines):
                        line_segments.append(problem_lines[line_idx])
                    else:
                        line_segments.append("")  # 补齐空白
                output.append("   ".join(line_segments))
            output.append("")  # 题目组间空行

        return '\n'.join(output)


if __name__ == "__main__":
    # 示例：一行显示3个带步骤的题目
    generator = SubtractionProblemGenerator(
        num_problems=200,
        per_row=3,
        print_steps=True
    )
    print(generator.generate())