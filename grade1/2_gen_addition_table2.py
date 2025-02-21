import matplotlib.pyplot as plt
import random
import os
from datetime import datetime


# 删除已存在的文件
def delete_existing_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)  # 删除文件
        print(f"文件 {file_path} 已删除。")


# 生成带时间戳的文件名
def generate_file_name():
    current_time = datetime.now()
    timestamp = current_time.strftime("%m%d%H%M%S")  # 获取当前时间，格式为 月日时分秒
    file_name = f'random_addition_subtraction_table_{timestamp}.png'
    return file_name


# 生成随机的加法和减法题目，结果不显示
def generate_random_addition_subtraction(num_problems=20, greater_than_10_ratio=0.7, generate_subtraction=False):
    problems = []
    count_gt_10 = int(num_problems * greater_than_10_ratio)  # 大于10的题目数
    count_le_10 = num_problems - count_gt_10  # 小于等于10的题目数

    # 如果生成减法题目
    if generate_subtraction:
        # 生成减法题目（从20开始减）
        while len(problems) < num_problems:
            a = random.randint(11, 20)  # 从大于等于11的数字开始
            b = random.randint(1, a)  # 保证结果为正数
            problems.append(f"{a}-{b}=")

    # 如果只生成加法题目
    else:
        # 生成大于10且小于等于20的加法题目
        while len(problems) < count_gt_10:
            a = random.randint(1, 20)  # 生成第一个加数，a 可以是 1 到 20 的任意数
            b = random.randint(1, 20)  # 生成第二个加数，b 也可以是 1 到 20 的任意数
            if a + b >= 11 and a + b <= 20:  # 保证加法结果在 11 到 20 之间
                problems.append(f"{a}+{b}=")

        # 生成小于等于10的加法题目
        while len(problems) < num_problems:
            a = random.randint(1, 9)  # 生成加数 a 小于等于 9
            b = random.randint(1, 9)  # 生成加数 b 小于等于 9
            if a + b <= 10:  # 保证结果小于等于10
                problems.append(f"{a}+{b}=")

    random.shuffle(problems)  # 随机打乱题目顺序
    return problems


# 绘制加法和减法题目表格并保存为图片
def draw_addition_subtraction_table(problems, num_columns=4, line_spacing=1.2, dpi=600):
    # 生成带时间戳的文件名
    file_path = generate_file_name()

    # 删除已存在的文件（如果有的话）
    delete_existing_file(file_path)

    # 计算行数
    num_rows = (len(problems) + num_columns - 1) // num_columns  # 向上取整计算行数

    # 构建表格数据，确保每行有 num_columns 列
    table_data = []
    for i in range(num_rows):
        row = problems[i * num_columns:(i + 1) * num_columns]  # 获取一行数据
        # 如果某行不足 num_columns 列，补充空值
        if len(row) < num_columns:
            row.extend([''] * (num_columns - len(row)))  # 补充空值
        table_data.append(row)

    # 创建图形
    fig, ax = plt.subplots(figsize=(12, 10))  # 增加图表的尺寸，确保足够大
    ax.axis('tight')
    ax.axis('off')

    # 创建表格（去掉交替颜色）
    table = ax.table(cellText=table_data, loc='center', cellLoc='center',
                     colLabels=[f"Col {i + 1}" for i in range(num_columns)],
                     rowLabels=[f"Row {i + 1}" for i in range(num_rows)])

    # 设置字体和列宽
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.auto_set_column_width(col=list(range(num_columns)))

    # 设置行间距，通过调整行高度
    for row in table.get_celld().values():
        row.set_height(line_spacing)  # 设置每行的高度以控制行间距

    # 保存为高清图片，增加dpi
    plt.savefig(file_path, bbox_inches='tight', dpi=dpi)  # 使用600dpi来确保高清效果
    plt.show()


# 执行函数
def main():
    num_problems = 100  # 生成题目数
    greater_than_10_ratio = 0.7  # 大于10的题目比例
    generate_subtraction = False  # 是否生成减法题目
    line_spacing = 0.05  # 控制行间距
    problems = generate_random_addition_subtraction(num_problems, greater_than_10_ratio, generate_subtraction)
    draw_addition_subtraction_table(problems, line_spacing=line_spacing, dpi=600)  # 使用高分辨率


# 执行主函数
main()
