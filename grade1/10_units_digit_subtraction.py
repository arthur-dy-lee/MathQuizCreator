import random
from itertools import zip_longest


def create_equation():
    # 生成十位数（1-9）和个位数（0-8）
    tens = random.randint(2, 9)
    ones = random.randint(0, 8)
    a = tens * 10 + ones
    # 确保b大于个位数且结果非负
    b = random.randint(ones + 1, 9)
    return f"{a} - {b} = __"


def generate_row_numbered_questions(num=1500, per_row=3):
    # 生成题目列表
    questions = [create_equation() for _ in range(num)]

    # 按每行题目数分组
    grouped = zip_longest(*[iter(questions)] * per_row, fillvalue='')

    output = []
    for line_num, group in enumerate(grouped, start=1):
        # 格式化学题目行
        equations = "\t".join([f"{eq:18}" for eq in group])
        numbered_line = f"{line_num:03d}.\t{equations}"
        output.append(numbered_line)

        # 生成下划线行（每个题目下方对齐）
        underline = "\t".join([f"{'___________':18}" for _ in group])
        underline_line = f"    \t{underline}"  # 用空格代替行号保持对齐
        output.append(underline_line)

    return "\n".join(output)


# 生成并打印500道题，每行3题
print(generate_row_numbered_questions())