import random


class ArithmeticProblemGenerator:
    def __init__(self, num_problems, lines_per_problem=2, problems_per_line=3):
        self.num_problems = num_problems
        self.lines_per_problem = lines_per_problem
        self.problems_per_line = problems_per_line
        self.problems = []
        self.answers = []

    def generate_problems(self):
        # 定义符号集合（包括△☆☼☽等）
        symbols = ['△', '☆', '☼', '☽', '♡', '♧', '♤', '♢', '♣', '♥', '♦', '♠']

        for i in range(self.num_problems):
            problem_type = random.choice([1, 2])

            # 随机选择两个不同的符号
            symbol1, symbol2 = random.sample(symbols, 2)

            if problem_type == 1:
                # 类型1: A - a = B - b
                # 确保所有值在0-100之间且无负数
                for _ in range(100):  # 添加最大尝试次数
                    a = random.randint(1, 100)  # 随机数a (1-100)
                    b = random.randint(1, 100)  # 随机数b (1-100)

                    # 确保B足够大，避免负数
                    min_B = max(a, b)
                    if min_B > 100:
                        continue

                    B = random.randint(min_B, 100)

                    # 计算A和结果
                    result = B - b
                    A = result + a

                    # 检查A是否超过100
                    if A <= 100:
                        break
                else:
                    # 如果100次尝试都失败，使用安全值
                    a = random.randint(1, 50)
                    b = random.randint(1, 50)
                    B = random.randint(max(a, b), 100)
                    result = B - b
                    A = result + a

                # 存储问题和答案
                self.problems.append(f"{i + 1}. {symbol1} - {a} = {symbol2} - {b}")
                self.problems.append(f"   {symbol1} 〇 {symbol2}")

                # 比较关系：A = B - b + a = B + (a - b)
                comparison = '>' if a > b else '<' if a < b else '='
                self.answers.append((result, comparison))

            else:
                # 类型2: A - a = B + b
                # 确保所有值在0-100之间且无负数
                for _ in range(100):  # 添加最大尝试次数
                    a = random.randint(1, 100)  # 随机数a (1-100)
                    b = random.randint(1, 100)  # 随机数b (1-100)

                    # 计算结果的最小值和最大值
                    min_result = b  # 确保B = result - b >= 0
                    max_result = 100 - a  # 确保A = result + a <= 100

                    # 如果范围无效，重新生成
                    if min_result > max_result:
                        continue

                    result = random.randint(min_result, max_result)

                    # 计算B和A
                    B = result - b
                    A = result + a

                    # 检查是否有效
                    if 0 <= B <= 100 and 0 <= A <= 100:
                        break
                else:
                    # 如果100次尝试都失败，使用安全值
                    a = random.randint(1, 50)
                    b = random.randint(1, 50)
                    result = random.randint(b, 100 - a)
                    B = result - b
                    A = result + a

                # 存储问题和答案
                self.problems.append(f"{i + 1}. {symbol1} - {a} = {symbol2} + {b}")
                self.problems.append(f"   {symbol1} 〇 {symbol2}")

                # 比较关系：A = B + b + a > B
                self.answers.append((result, '>'))

    def display_problems(self):
        # 计算每道题占用的行数（题目行+比较符号行）
        lines_per_problem = 2

        # 计算总行数（每组题目）
        total_lines = lines_per_problem + self.lines_per_problem

        # 计算需要多少组题目（每组包含problems_per_line个题目）
        num_groups = (self.num_problems + self.problems_per_line - 1) // self.problems_per_line

        for group_idx in range(num_groups):
            # 计算当前组的起始题目索引
            start_idx = group_idx * self.problems_per_line
            end_idx = min(start_idx + self.problems_per_line, self.num_problems)

            # 打印当前组的所有题目
            for line_idx in range(total_lines):
                for problem_idx in range(start_idx, end_idx):
                    # 计算题目在列表中的位置
                    problem_line_idx = problem_idx * lines_per_problem * 2 + line_idx

                    # 如果当前行是空行，打印空行
                    if line_idx >= lines_per_problem:
                        print(" " * 30, end="")  # 30字符宽度的空位
                    else:
                        # 获取题目行并打印
                        problem_line = self.problems[problem_idx * 2 + line_idx]
                        print(f"{problem_line:<30}", end="")
                print()  # 换行

            # 每组题目后添加额外的空行
            for _ in range(self.lines_per_problem):
                print()

    def display_answers(self):
        print("\n答案：")
        for i, (result, comparison) in enumerate(self.answers):
            print(f"{i + 1}. 等式结果: {result}, 比较符号: {comparison}")


def main():
    # 创建题目生成器（10道题，每题后空2行，每行3道题）
    generator = ArithmeticProblemGenerator(
        num_problems=600,
        lines_per_problem=1,
        problems_per_line=3
    )

    # 生成题目
    generator.generate_problems()

    # 显示题目
    print("生成的题目：")
    generator.display_problems()

    # 显示答案
    generator.display_answers()


if __name__ == "__main__":
    main()
