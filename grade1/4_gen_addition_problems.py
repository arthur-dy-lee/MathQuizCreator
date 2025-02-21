import random


def generate_addition_problems(num_problems=1000):
    """
    结果范围：加法的结果
    sum = a + b
    应该大于  10，但不超过 20。
    输出格式：每行显示 4 个题目，且每个题目以 题号: a + b = ? 的格式输出。
    结果不展示：题目仅显示加法表达式和题号，不显示结果。
    """

    problems = []

    # 生成指定数量的题目
    for i in range(1, num_problems + 1):
        while True:
            a = random.randint(0, 9)  # 生成第一个个位数
            b = random.randint(0, 9)  # 生成第二个个位数
            sum_result = a + b

            # 确保结果大于10且小于等于20
            if 10 < sum_result <= 20:
                problems.append(f"{i}: {a} + {b} = (  )  ")
                break

    return problems


def print_problems_in_rows(problems, row_length=4):
    # 按行输出，每行最多显示4个题目
    line_count = 0  # 记录当前输出的行数
    for i in range(0, len(problems), row_length):
        print("    ".join(problems[i:i + row_length]))
        line_count += 1

        # 每25行（即100题）后插入两个空行
        if line_count % 25 == 0:  # 100题/4题每行 = 25行
            print("\n\n")


# 生成1000个加法题目
problems = generate_addition_problems()

# 打印输出所有题目，每行4个，间隔每100个题目后加2个空行
print_problems_in_rows(problems)
