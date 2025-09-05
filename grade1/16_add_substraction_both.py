import random
import argparse

"""
帮我生成python加减法算法，要求：1. 计算结果不超过100，不允许有负数出现。2. 退位减法，进位加法每100题占80%，这个参数可以通过入参可以调，默认0.8。  
3. 结果要在最后总一打印，要带题目数字标号，和题目一一对应。  4. 其它参数：参数:
num_problems -- 生成总题目数量
lines_per_problem -- 每题后的空行数 (默认3)
problems_per_line -- 每行题目数 (默认4)，
每个题都带有数字标号。
输出的题目结果要对齐。最后的结果即等号右边带2个下划线。
"""


def generate_math_problems(num_problems, carry_ratio=0.8, lines_per_problem=3, problems_per_line=4):
    problems = []
    answers = []

    # 计算需要多少进位加法和退位减法题目
    special_count = int(num_problems * carry_ratio)
    normal_count = num_problems - special_count

    # 生成进位加法和退位减法题目
    for _ in range(special_count):
        problem_type = random.choice(['addition', 'subtraction'])

        if problem_type == 'addition':
            # 生成需要进位的加法
            while True:
                a = random.randint(10, 99)
                b = random.randint(1, 99)
                if a + b <= 100 and (a % 10 + b % 10) >= 10:
                    # 格式化数字，确保对齐
                    a_str = f"{a:2d}"
                    b_str = f"{b:2d}"
                    problems.append(f"{a_str} + {b_str} = ")
                    answers.append(a + b)
                    break
        else:
            # 生成需要退位的减法
            while True:
                a = random.randint(10, 99)
                b = random.randint(1, a)  # 确保结果不为负数
                if (a % 10) < (b % 10):  # 确保需要退位
                    # 格式化数字，确保对齐
                    a_str = f"{a:2d}"
                    b_str = f"{b:2d}"
                    problems.append(f"{a_str} - {b_str} = ")
                    answers.append(a - b)
                    break

    # 生成普通加减法题目
    for _ in range(normal_count):
        problem_type = random.choice(['addition', 'subtraction'])

        if problem_type == 'addition':
            # 生成普通加法
            while True:
                a = random.randint(1, 99)
                b = random.randint(1, 99)
                if a + b <= 100 and (a % 10 + b % 10) < 10:  # 不需要进位
                    # 格式化数字，确保对齐
                    a_str = f"{a:2d}"
                    b_str = f"{b:2d}"
                    problems.append(f"{a_str} + {b_str} = ")
                    answers.append(a + b)
                    break
        else:
            # 生成普通减法
            while True:
                a = random.randint(10, 99)
                b = random.randint(1, a)  # 确保结果不为负数
                if (a % 10) >= (b % 10):  # 不需要退位
                    # 格式化数字，确保对齐
                    a_str = f"{a:2d}"
                    b_str = f"{b:2d}"
                    problems.append(f"{a_str} - {b_str} = ")
                    answers.append(a - b)
                    break

    # 打乱题目顺序
    combined = list(zip(problems, answers))
    random.shuffle(combined)
    problems, answers = zip(*combined)

    return list(problems), list(answers)


def format_output(problems, answers, lines_per_problem, problems_per_line):
    output = ""
    answer_output = "\n答案:\n"

    # 计算题号的最大宽度
    max_index_width = len(str(len(problems))) + 1

    # 计算每个问题的最大宽度
    max_problem_width = max(len(problem) for problem in problems) + 2

    # 格式化题目
    for i, problem in enumerate(problems, 1):
        # 添加题号并确保对齐
        index_str = f"{i}.".ljust(max_index_width)
        formatted_problem = f"{index_str} {problem}__"

        # 添加到输出
        output += formatted_problem.ljust(max_problem_width + max_index_width + 2)

        # 换行逻辑
        if i % problems_per_line == 0:
            output += "\n" * lines_per_problem
        else:
            output += " " * 4  # 题目之间的间距

    # 格式化答案
    for i, answer in enumerate(answers, 1):
        index_str = f"{i}.".ljust(max_index_width)
        answer_output += f"{index_str} {answer:2d}".ljust(max_problem_width + max_index_width)
        if i % problems_per_line == 0:
            answer_output += "\n"

    return output + answer_output


def main():
    parser = argparse.ArgumentParser(description='生成加减法题目')
    parser.add_argument('--num_problems', type=int, default=600, help='总题目数量')
    parser.add_argument('--carry_ratio', type=float, default=0.8, help='进位加法和退位减法占比')
    parser.add_argument('--lines_per_problem', type=int, default=1, help='每题后的空行数')
    parser.add_argument('--problems_per_line', type=int, default=4, help='每行题目数')

    args = parser.parse_args()

    problems, answers = generate_math_problems(
        args.num_problems,
        args.carry_ratio,
        args.lines_per_problem,
        args.problems_per_line
    )

    result = format_output(problems, answers, args.lines_per_problem, args.problems_per_line)
    print(result)


if __name__ == "__main__":
    main()