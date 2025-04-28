import numpy as np
from typing import List


class AlignedMultiplicationQuiz:
    """支持大间距的两位数对齐版乘法题生成器"""

    def __init__(self, total=1200, per_line=4, min_num=2, max_num=9):
        self.total = total
        self.per_line = per_line
        self.min_num = min_num
        self.max_num = max_num
        self.col_width = 11  # 保持原列宽
        self.problem_space = "    "  # 题目间4个空格

    def generate(self) -> List[str]:
        """生成带大间距的题目"""
        a = np.random.randint(self.min_num, self.max_num + 1, self.total)
        b = np.random.randint(self.min_num, self.max_num + 1, self.total)
        types = np.random.randint(0, 3, self.total)

        problems = []
        for x, y, t in zip(a, b, types):
            product = x * y
            if t == 0:  # __ × b = c
                prob = f"__ × {y:2d} = {product:2d}".ljust(self.col_width)
            elif t == 1:  # a × __ = c
                prob = f"{x:2d} × __ = {product:2d}".center(self.col_width)
            else:  # a × b = __
                prob = f"{x:2d} × {y:2d} = __".rjust(self.col_width)
            problems.append(prob)
        return self._format(problems)

    def _format(self, problems: List[str]) -> List[str]:
        """带大间距的分块排版"""
        return [
            f"({idx + 1})  " + self.problem_space.join(problems[i:i + self.per_line])
            for idx, i in enumerate(range(0, self.total, self.per_line))
        ]


# 使用示例
if __name__ == "__main__":
    generator = AlignedMultiplicationQuiz(total=2000, per_line=4)
    print("带大间距的两位数对齐版乘法题：\n" + "=" * 60)
    for line in generator.generate():
        print(line)