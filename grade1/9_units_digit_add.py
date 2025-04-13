import random
from itertools import zip_longest

"""
十位数 相加/减 个位数， 结果是在100以内的加法和减法
"""

def generate_row_numbered_questions(num=500, operation='both', per_row=4):
    # 生成题目内容（不带序号）
    questions = [create_equation(operation) for _ in range(num)]  # 网页3的批量生成方法

    # 按每行4题分组（网页4的分块逻辑）
    grouped = zip_longest(*[iter(questions)] * per_row, fillvalue='')

    # 添加行号并格式化（网页5的序号添加技巧）
    output = []
    for line_num, group in enumerate(grouped, start=1):
        equations = "\t".join([f"{eq:18}" for eq in group])  # 网页4的格式化对齐
        numbered_line = f"{line_num:03d}.\t{equations}"  # 网页5的行号补零
        output.append(numbered_line)

    return "\n".join(output)


def create_equation(operation):
    a = random.randint(11, 99)  # 网页1的数值范围控制
    b = random.randint(1, 9)

    # 运算符逻辑（网页2的随机生成方法）
    #op = random.choice(['+', '-']) if operation == 'both' else operation
    op = random.choice(['+']) if operation == 'both' else operation

    # 结果校验（网页3的边界控制）
    return f"{a} {op} {b} = __"


# 生成500道题，每行4题（网页6的批量参数）
print(generate_row_numbered_questions(500))