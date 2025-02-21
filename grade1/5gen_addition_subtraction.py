import random


def generate_addition_problems(num_problems=1000):
    """
    生成加法题目，要求：
    - 和大于 10，但不超过 20
    - 输出格式：每行显示 4 个题目，且每个题目以题号: a + b = ? 的格式输出。
    """
    problems = []

    for i in range(1, num_problems + 1):
        while True:
            a = random.randint(0, 9)  # 生成第一个个位数
            b = random.randint(0, 9)  # 生成第二个个位数
            sum_result = a + b

            # 确保加法结果大于 10 且小于等于 20
            if 10 < sum_result <= 20:
                problems.append(f"{i:3}: {a:2} + {b:2} =  ")
                break

    return problems


def generate_subtraction_problems(num_problems=1000):
    """
    生成减法题目，有两种形式：
    1. ( ) - b = result，减数 b 为 1 到 9 之间的随机数，结果为个位数
    2. a - ( ) = result，减数 b 也是从 1 到 9 之间的随机数
    """
    problems = []

    for i in range(1, num_problems + 1):
        while True:
            form = random.choice([1, 2])  # 选择题目形式：1 或 2

            if form == 1:
                # 形式1: ( ) - b = result
                a = random.randint(11, 20)  # 被减数从 11 到 20
                b = random.randint(1, 9)    # 减数从 1 到 9
                result = a - b
                problems.append(f"{i:3}: (  ) - {b:2} = {result:2}")

            else:
                # 形式2: a - ( ) = result
                a = random.randint(11, 20)  # 被减数从 11 到 20
                result = random.randint(0, 9)  # 结果是个位数
                b = a - result  # 计算减数
                if b >= 1:  # 确保减数 b 是 1 到 9 之间的数
                    problems.append(f"{i:3}: {a:2} - (  ) = {result:2}")
            break

    return problems


def print_problems_in_rows(problems, row_length=4):
    """
    将题目按行输出，每行最多显示4个题目
    每25行（即100题）后插入两个空行
    """
    line_count = 0
    for i in range(0, len(problems), row_length):
        print("    ".join(problems[i:i + row_length]))
        line_count += 1

        # 每25行（即100题）后插入两个空行
        if line_count % 25 == 0:
            print("\n\n")


# 生成1000个加法题目
addition_problems = generate_addition_problems()

# 生成1000个减法题目
subtraction_problems = generate_subtraction_problems()

# 将加法和减法题目合并并打乱
all_problems = addition_problems + subtraction_problems
random.shuffle(all_problems)  # 打乱题目顺序

# 打印混合后的所有题目，每行4个，间隔每100个题目后加2个空行
print_problems_in_rows(all_problems)
