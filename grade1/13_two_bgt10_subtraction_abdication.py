import random


class BorrowSubtractionGenerator:
    """两位数退位减法生成器（支持退位比例控制）"""

    def __init__(self, total=100, borrow_ratio=90, per_line=4, line_num_start=1):
        """
        :param total: 总题目数
        :param borrow_ratio: 退位题占比(0-100)
        :param per_line: 每行题目数
        :param line_num_start: 起始行号
        """
        self.total = total
        self.borrow_ratio = borrow_ratio / 100
        self.per_line = per_line
        self.line_num_start = line_num_start

    def _generate_valid_pair(self):
        """生成符合退位条件的两位数减法对"""
        while True:
            # 决定是否生成退位题（基于网页1的退位条件）
            require_borrow = random.random() < self.borrow_ratio

            if require_borrow:
                # 退位情况（网页1算法优化）
                a_tens = random.randint(2, 9)  # 被减数十位 ≥2
                b_tens = random.randint(1, a_tens - 1)  # 减数十位 < 被减数十位
                a_units = random.randint(0, 8)  # 被减数个位 ≤8
                b_units = random.randint(a_units + 1, 9)  # 减数个位 > 被减数个位（必须退位）
            else:
                # 非退位情况（网页6的非退位逻辑）
                a_tens = random.randint(1, 9)
                b_tens = random.randint(1, a_tens)
                a_units = random.randint(0 if b_tens < a_tens else 1, 9)
                b_units = random.randint(0, a_units)

            minuend = a_tens * 10 + a_units
            subtrahend = b_tens * 10 + b_units

            # 结果验证（确保非负数）
            if minuend <= subtrahend:
                continue

            return f"{minuend:02} - {subtrahend:02} =____", require_borrow

    def _batch_generate(self):
        """批量生成题目"""
        exercises = []
        borrow_count = 0
        while len(exercises) < self.total:
            problem, is_borrow = self._generate_valid_pair()
            exercises.append(problem)
            if is_borrow:
                borrow_count += 1
        return exercises, borrow_count

    def _format_lines(self, problems):
        """格式化输出（基于网页5的排版逻辑）"""
        chunked = [problems[i:i + self.per_line]
                   for i in range(0, len(problems), self.per_line)]
        return [
            f"({line_num})  " + "    ".join(line_problems)
            for line_num, line_problems in enumerate(chunked, self.line_num_start)
        ]

    def generate(self):
        """生成题目并返回统计信息"""
        problems, borrow_count = self._batch_generate()
        formatted = self._format_lines(problems)

        # 统计信息（参考网页7的验证逻辑）
        stats = {
            "total": self.total,
            "borrow_percent": round(borrow_count / self.total * 100, 1),
            "sample": problems[:3]  # 示例题目
        }
        return formatted, stats


# 使用示例
if __name__ == "__main__":
    generator = BorrowSubtractionGenerator(
        total=1000,
        borrow_ratio=90,
        per_line=4,
        line_num_start=1
    )

    problems, stats = generator.generate()

    # 打印题目
    print("生成的减法练习题：\n" + "=" * 40)
    for line in problems:
        print(line)

    # 打印统计
    print("\n统计报告：")
    print(f"总题数：{stats['total']}")
    print(f"退位题占比：{stats['borrow_percent']}%")
    print(f"示例题目：{', '.join(stats['sample'])}")