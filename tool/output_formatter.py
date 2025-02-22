"""
@Author: arthur
@Email: arthur.dy.lee@gmail.com
@Date: 2/22/2025 11:59 AM
@Last Modified by: arthur
@Last Modified time: 2/22/2025 11:59 AM
"""
class OutputFormatter:
    def __init__(self,
                 per_line=4,
                 line_num_format="({})",
                 column_width=10,
                 line_num_start=1):
        """
        :param per_line: 每行显示题目数
        :param line_num_format: 题号格式模板，如"({:0>2d})"
        :param column_width: 每列字符宽度
        :param line_num_start: 起始题号
        """
        self.per_line = per_line
        self.line_num_format = line_num_format
        self.column_width = column_width
        self.line_num_start = line_num_start

    def align_element(self, element, width=None):
        """通用元素对齐方法"""
        width = width or self.column_width
        return f"{str(element):^{width}}"

    def format_line_number(self, current_index):
        """动态生成题号"""
        actual_num = self.line_num_start + current_index//self.per_line
        return self.line_num_format.format(actual_num)

    def group_elements(self, elements):
        """元素分组方法"""
        return [elements[i:i+self.per_line]
                for i in range(0, len(elements), self.per_line)]

    def build_line(self, line_elements, line_index):
        """构建单行输出"""
        line_num = self.format_line_number(line_index)
        aligned = [self.align_element(e) for e in line_elements]
        return f"{line_num}  {'  '.join(aligned)}"

    def format_output(self, elements):
        """执行完整格式化"""
        grouped = self.group_elements(elements)
        return [self.build_line(group, idx*self.per_line)
                for idx, group in enumerate(grouped)]
