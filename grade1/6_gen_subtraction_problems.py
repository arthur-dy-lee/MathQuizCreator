import random


class MathProblemGenerator:
    def __init__(self, num_problems=1000, addition_ratio=0.6):
        """
        初始化问题生成器，设置题目总数和加法比例
        :param num_problems: 题目数量
        :param addition_ratio: 每100题中加法题目的占比 (0 到 1 之间)
        """
        self.num_problems = num_problems
        self.addition_ratio = addition_ratio
        self.problems = []
        self.current_problem_number = 1  # 题号从1开始

    def generate_addition_problem(self):
        """
        生成加法题目，要求：
        - 和大于 10，但不超过 20
        - 2个个位数相加
        - 3种加法题目形式：
            1. a + b = ?
            2. (   ) + 个位数 = 结果
            3. 个位数 + (   ) = 结果
        """
        while True:
            # 生成两个个位数，确保加法结果在10到20之间
            a = random.randint(1, 9)  # 第一个个位数
            b = random.randint(1, 9)  # 第二个个位数
            sum_result = a + b

            if 10 <= sum_result <= 20:
                # 随机选择加法题目形式
                form = random.choice([1, 2, 3])  # 1: a + b, 2: (  ) + b, 3: a + (  )

                if form == 1:
                    # 形式1: a + b = ?
                    self.problems.append(f"{self.current_problem_number:4}: {a:2} + {b:2} = (  )")
                elif form == 2:
                    # 形式2: (  ) + b = result
                    self.problems.append(f"{self.current_problem_number:4}: (  ) + {b:2} = {sum_result:2}")
                elif form == 3:
                    # 形式3: a + (  ) = result
                    self.problems.append(f"{self.current_problem_number:4}: {a:2} + (  ) = {sum_result:2}")

                # 题号递增
                self.current_problem_number += 1
                break

    def generate_subtraction_problem(self):
        """
        生成减法题目，有两种形式：
        1. ( ) - b = result
        2. a - ( ) = result
        """
        while True:
            form = random.choice([1, 2])  # 选择题目形式：1 或 2

            if form == 1:
                a = random.randint(11, 20)  # 被减数从 11 到 20
                b = random.randint(1, 9)  # 减数从 1 到 9
                result = a - b
                if result >= 0 and result <= 9:
                    self.problems.append(f"{self.current_problem_number:4}: (  ) - {b:2} = {result:2}")
                    self.current_problem_number += 1
                    break

            elif form == 2:
                a = random.randint(11, 20)  # 被减数从 11 到 20
                result = random.randint(0, 9)  # 结果是个位数
                b = a - result  # 计算减数
                if b >= 1 and b <= 9:  # 确保减数 b 是 1 到 9 之间的数
                    self.problems.append(f"{self.current_problem_number:4}: {a:2} - (  ) = {result:2}")
                    self.current_problem_number += 1
                    break

    def generate_problems_for_block(self, block_start, block_size=100):
        """
        为每100题块生成加法和减法题目，确保加法题目占比60%，减法题目占比40%
        """
        num_addition = int(block_size * self.addition_ratio)  # 每块中加法题目数量
        num_subtraction = block_size - num_addition  # 每块中减法题目数量

        # 生成加法题目
        for _ in range(num_addition):
            self.generate_addition_problem()

        # 生成减法题目
        for _ in range(num_subtraction):
            self.generate_subtraction_problem()

    def generate_all_problems(self):
        """
        生成所有题目，根据加法比例生成相应数量的加法和减法题目
        每100题块生成加法和减法题目
        """
        block_size = 100
        num_blocks = self.num_problems // block_size  # 计算题目块的数量

        # 生成每个题目块中的题目
        for block in range(num_blocks):
            block_start = block * block_size + 1
            self.generate_problems_for_block(block_start, block_size)

    def print_problems_in_rows(self, row_length=4):
        """
        将题目按行输出，每行最多显示4个题目
        每25行（即100题）后插入两个空行
        """
        line_count = 0
        for i in range(0, len(self.problems), row_length):
            print("   ".join(self.problems[i:i + row_length]))  # 用三个空格分隔题目
            line_count += 1

            # 每25行（即100题）后插入两个空行
            if line_count % 25 == 0:
                print("\n")


def main():
    # 创建问题生成器对象，设置加法占比为60%
    problem_generator = MathProblemGenerator(num_problems=1000, addition_ratio=0.6)

    # 生成所有题目
    problem_generator.generate_all_problems()

    # 打印所有题目
    problem_generator.print_problems_in_rows()


if __name__ == "__main__":
    main()
