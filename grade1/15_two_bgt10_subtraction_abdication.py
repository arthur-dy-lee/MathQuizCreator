import random


def generate_subtraction_problems(num_problems, lines_per_problem=2, problems_per_line=4):
    """
    生成纯两位数退位减法题目

    参数:
    num_problems -- 题目数量
    lines_per_problem -- 每题后的空行数 (默认3)
    problems_per_line -- 每行题目数 (默认4)

    返回:
    (题目列表, 答案列表)
    """
    problems = []
    answers = []

    for i in range(num_problems):
        while True:
            # 生成被减数 (20-99)
            a = random.randint(20, 99)
            a_tens = a // 10
            a_ones = a % 10

            # 确保被减数个位0-8 (确保有比它大的个位数)
            if a_ones > 8:
                continue

            # 生成减数的十位 (1到被减数十位-1，保证结果正两位数)
            b_tens = random.randint(1, a_tens - 1)

            # 生成减数的个位 (比被减数个位大1到9)
            b_ones = random.randint(a_ones + 1, 9)

            b = b_tens * 10 + b_ones

            # 计算答案
            answer = a - b

            # 确保是标准的退位减法（个位不够减）
            if b_ones > a_ones and answer > 0:
                # 格式化为题目和答案
                problem = f"({i + 1}) {a} - {b} = __"
                ans = f"{answer}"

                problems.append(problem)
                answers.append(ans)
                break

    return problems, answers


def format_problems(problems, answers, lines_per_problem=2, problems_per_line=4):
    """
    格式化题目和答案

    参数:
    problems -- 题目列表
    answers -- 答案列表
    lines_per_problem -- 每题后的空行数
    problems_per_line -- 每行题目数

    返回:
    格式化后的字符串
    """
    # 检查输入长度
    if len(problems) != len(answers):
        raise ValueError("题目和答案数量不一致")

    formatted_lines = []
    num_problems = len(problems)

    # 添加题目部分 (每行固定题数)
    for i in range(0, num_problems, problems_per_line):
        # 获取当前行的题目
        line_problems = problems[i:i + problems_per_line]
        # 创建题目行 (等宽对齐)
        problem_line = "  ".join(line_problems)
        formatted_lines.append(problem_line)

        # 添加指定空行
        formatted_lines.extend([""] * lines_per_problem)

    # 添加答案部分（所有答案在一行显示）
    formatted_lines.append("\n答案：")

    # 创建带括号的答案列表
    answer_list = [f"({i + 1}) {ans}" for i, ans in enumerate(answers)]

    # 所有答案在一行显示
    formatted_lines.append("    ".join(answer_list))

    return "\n".join(formatted_lines)


# 示例用法
if __name__ == "__main__":
    # 生成20道纯两位数退位减法题目
    problems, answers = generate_subtraction_problems(1000)

    # 格式化输出 (每行4题，每题后3空行)
    result = format_problems(problems, answers)
    print(result)