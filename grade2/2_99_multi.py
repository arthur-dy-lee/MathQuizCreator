import numpy as np
from typing import List


class OptimizedMultiplicationGenerator:
    """优化版乘法题生成器（排除乘数1）"""

    def __init__(self, total: int = 100, per_line: int = 4):
        """
        :param total: 总题目数量
        :param per_line: 每行显示题数
        """
        self.total = total
        self.per_line = per_line
        self.min_num = 2  # 最小乘数
        self.max_num = 9  # 最大乘数

    def generate(self) -> List[str]:
        """批量生成题目（允许重复但排除乘数1）"""
        # 使用NumPy批量生成随机数（网页5性能优化方案）
        a = np.random.randint(self.min_num, self.max_num + 1, self.total)
        b = np.random.randint(self.min_num, self.max_num + 1, self.total)
        return [f"{x}×{y}=__" for x, y in zip(a, b)]

    def format_output(self, problems: List[str]) -> str:
        """优化排版逻辑（网页1格式参考）"""
        chunk_size = self.per_line
        return '\n'.join(
            f"({i // chunk_size + 1})  " + "       ".join(problems[i:i + chunk_size])
            for i in range(0, self.total, chunk_size)
        )


# 使用示例
if __name__ == "__main__":
    # 生成200题，每行3题（网页6参数设置思路）
    generator = OptimizedMultiplicationGenerator(total=2000, per_line=4)
    problems = generator.generate()

    print("优化版乘法练习题（无乘数1）：\n" + "=" * 50)
    print(generator.format_output(problems))