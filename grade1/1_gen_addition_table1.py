import matplotlib.pyplot as plt
import os

# 生成加法表，计算到20
def generate_addition_table():
    max_number = 20
    table = []

    # 对于每个加数 i (从 2 到 9)
    for i in range(2, 10):
        row = []
        j = 1
        # 只保留加法结果小于等于20的项
        while i + j <= max_number:
            row.append(f"{i}+{j}={i + j}")
            j += 1
        table.append(row)

    # 计算最大列数（最大加法项的数量）
    max_columns = max(len(row) for row in table)

    # 填充每一行使其长度一致
    for i in range(len(table)):
        while len(table[i]) < max_columns:
            table[i].append("")  # 填充空字符串

    return table


# 删除已存在的文件
def delete_existing_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)  # 删除文件
        print(f"文件 {file_path} 已删除。")


# 绘制加法表格并保存为高清图片
def draw_addition_table(line_spacing=0.05, dpi=300):
    # 文件路径
    file_path = 'addition_table_20.png'

    # 删除已存在的文件（如果有的话）
    delete_existing_file(file_path)

    # 获取加法表
    table = generate_addition_table()

    # 确定图表大小
    fig, ax = plt.subplots(figsize=(12, 10))  # 增加图表的尺寸，使其更加宽大
    ax.axis('tight')
    ax.axis('off')

    # 转置表格，使每列变为每个固定数字（2-9）
    table_data = list(zip(*table))  # 将行和列互换

    # 动态计算行数
    row_count = len(table_data)

    # 创建动态的 rowLabels
    row_labels = [f"{i}" for i in range(1, row_count + 1)]

    # 创建表格
    table = ax.table(cellText=table_data, loc='center', cellLoc='center', colLabels=[str(i) for i in range(2, 10)],
                     rowLabels=row_labels)

    # 调整行间距
    for row in table.get_celld().values():
        row.set_height(line_spacing)  # 设置每行的高度来控制行间距

    # 保存为高清图片，增加dpi
    plt.savefig(file_path, bbox_inches='tight', dpi=dpi)  # 使用更高的dpi
    plt.show()


# 执行绘制和保存高清图片
draw_addition_table(line_spacing=0.05, dpi=600)  # 使用600dpi来确保图像更清晰
