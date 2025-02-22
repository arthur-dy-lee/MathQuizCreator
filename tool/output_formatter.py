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
                 line_num_format="({:0>2d})",
                 column_width=12,
                 line_num_start=1):
        self.per_line = per_line
        self.line_num_format = line_num_format
        self.column_width = column_width
        self.line_num_start = line_num_start

    def _align_element(self, element):
        return f"{str(element):<{self.column_width}}"

    def format_line_number(self, current_index):
        actual_num = self.line_num_start + current_index//self.per_line
        return self.line_num_format.format(actual_num)

    def build_line(self, line_elements, line_index):
        line_num = self.format_line_number(line_index)
        aligned = [self._align_element(e) for e in line_elements]
        return f"{line_num}  {'  '.join(aligned)}"  # 标号后2空格

    def format_output(self, problems):
        return [self.build_line(problems[i:i+self.per_line], i)
                for i in range(0, len(problems), self.per_line)]
