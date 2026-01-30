"""
算术题生成器 - ArithmeticQuizGenerator
支持加减乘除，可配置各种参数，自动生成练习题和答案
"""

import random
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Set, Tuple, Optional


class Operation(Enum):
    """运算类型枚举"""
    ADD = auto()       # 加法
    SUB = auto()       # 减法
    MUL = auto()       # 乘法
    DIV = auto()       # 除法


class BlankPosition(Enum):
    """填空位置枚举"""
    FIRST = auto()     # 第一个数
    SECOND = auto()    # 第二个数
    RESULT = auto()    # 结果


@dataclass
class QuizConfig:
    """题目配置类"""
    # 基础参数
    total_questions: int = 999              # 总题数
    questions_per_row: int = 4              # 每行题数
    spaces_after_question: int = 3          # 题目间空格数
    blank_underscores: int = 2              # 下划线数量
    num_align_width: int = 2                # 数字对齐宽度（默认2位数对齐）

    # 运算类型
    operations: Set[Operation] = field(default_factory=lambda: {
        Operation.ADD, Operation.SUB, Operation.MUL, Operation.DIV
    })

    # 数值范围
    min_value: int = 0                      # 最小值
    max_value: int = 109                    # 最大值

    # 乘法控制
    multiplication_table_only: bool = False # 乘法是否仅限9*9乘法表

    # 比例控制
    add_sub_carry_ratio: float = 0.5        # 加减法进位/借位比例，默认50%
    mul_carry_ratio: float = 0.6            # 乘法进位比例（9×9以外），默认60%
    add_sub_group_ratio: float = 0.8        # 加减法组占比，默认80%


@dataclass
class Question:
    """单个题目"""
    number: int                # 题号
    a: int                     # 第一个操作数
    b: int                     # 第二个操作数
    result: int                # 结果
    operation: Operation       # 运算符
    blank_position: BlankPosition  # 填空位置

    def get_operator_symbol(self) -> str:
        """获取运算符号"""
        symbols = {
            Operation.ADD: '+',
            Operation.SUB: '-',
            Operation.MUL: '×',
            Operation.DIV: '÷'
        }
        return symbols[self.operation]

    def format_question(self, underscores: int = 2, num_width: int = 2) -> str:
        """格式化题目显示（带对齐）"""
        blank = '_' * underscores
        op = self.get_operator_symbol()

        # 格式化数字，右对齐
        a_str = str(self.a).rjust(num_width)
        b_str = str(self.b).rjust(num_width)
        r_str = str(self.result).rjust(num_width)
        blank_str = blank.rjust(num_width)

        if self.blank_position == BlankPosition.FIRST:
            return f"{blank_str} {op} {b_str} = {r_str}"
        elif self.blank_position == BlankPosition.SECOND:
            return f"{a_str} {op} {blank_str} = {r_str}"
        else:  # RESULT
            return f"{a_str} {op} {b_str} = {blank_str}"

    def get_answer(self) -> int:
        """获取答案"""
        if self.blank_position == BlankPosition.FIRST:
            return self.a
        elif self.blank_position == BlankPosition.SECOND:
            return self.b
        else:
            return self.result

    def format_answer(self, num_width: int = 2) -> str:
        """格式化答案显示"""
        return str(self.get_answer()).rjust(num_width)


class ArithmeticQuizGenerator:
    """算术题生成器"""

    def __init__(self, config: Optional[QuizConfig] = None):
        self.config = config or QuizConfig()
        self.questions: List[Question] = []
        self.num_width = self.config.num_align_width
        self.question_num_width = len(str(self.config.total_questions))

    def _has_carry_addition(self, a: int, b: int) -> bool:
        """判断加法是否有进位"""
        while a > 0 or b > 0:
            if (a % 10) + (b % 10) >= 10:
                return True
            a //= 10
            b //= 10
        return False

    def _has_borrow_subtraction(self, a: int, b: int) -> bool:
        """判断减法是否有借位"""
        while a > 0 or b > 0:
            if (a % 10) < (b % 10):
                return True
            a //= 10
            b //= 10
        return False

    def _is_within_99_table(self, a: int, b: int) -> bool:
        """判断乘法是否在9×9表内"""
        return 1 <= a <= 9 and 1 <= b <= 9

    def _generate_addition(self, need_carry: bool = False) -> Tuple[int, int, int]:
        """生成加法题"""
        max_val = self.config.max_value
        min_val = self.config.min_value

        for _ in range(100):
            a = random.randint(min_val, max_val)
            max_b = max_val - a
            if max_b < min_val:
                continue
            b = random.randint(min_val, max_b)

            if need_carry == self._has_carry_addition(a, b):
                return a, b, a + b

        a = random.randint(min_val, max_val // 2)
        b = random.randint(min_val, max_val - a)
        return a, b, a + b

    def _generate_subtraction(self, need_borrow: bool = False) -> Tuple[int, int, int]:
        """生成减法题"""
        max_val = self.config.max_value
        min_val = self.config.min_value

        for _ in range(100):
            a = random.randint(min_val, max_val)
            b = random.randint(min_val, a)
            c = a - b

            if c >= min_val and need_borrow == self._has_borrow_subtraction(a, b):
                return a, b, c

        a = random.randint(min_val, max_val)
        b = random.randint(min_val, a)
        return a, b, a - b

    def _generate_multiplication(self, need_carry: bool = False) -> Tuple[int, int, int]:
        """生成乘法题"""
        max_val = self.config.max_value
        min_val = self.config.min_value

        if self.config.multiplication_table_only:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            return a, b, a * b

        for _ in range(100):
            if need_carry:
                # 9×9以外的乘法
                a = random.randint(2, min(max_val, 99))
                if a <= 9:
                    max_b = min(max_val // max(a, 1), max_val)
                    if max_b <= 9:
                        continue
                    b = random.randint(10, max_b)
                else:
                    max_b = min(max_val // a, max_val)
                    if max_b < 1:
                        continue
                    b = random.randint(1, max_b)
            else:
                a = random.randint(1, 9)
                b = random.randint(1, 9)

            c = a * b
            if min_val <= c <= max_val and need_carry != self._is_within_99_table(a, b):
                return a, b, c

        a = random.randint(1, 9)
        b = random.randint(1, 9)
        return a, b, a * b

    def _generate_division(self) -> Tuple[int, int, int]:
        """生成除法题"""
        max_val = self.config.max_value
        min_val = self.config.min_value

        b = random.randint(max(1, min_val), max(1, min(max_val, 99)))
        max_c = max_val // b
        if max_c < min_val:
            b = random.randint(1, 9)
            max_c = max_val // b

        c = random.randint(max(min_val, 0), max(min_val, max_c))
        a = b * c
        return a, b, c

    def _determine_operation(self) -> Operation:
        """确定运算类型"""
        ops = self.config.operations
        add_sub_ops = {op for op in ops if op in {Operation.ADD, Operation.SUB}}
        mul_div_ops = {op for op in ops if op in {Operation.MUL, Operation.DIV}}

        if not add_sub_ops:
            return random.choice(list(mul_div_ops))
        if not mul_div_ops:
            return random.choice(list(add_sub_ops))

        if random.random() < self.config.add_sub_group_ratio:
            return random.choice(list(add_sub_ops))
        else:
            return random.choice(list(mul_div_ops))

    def _determine_carry_need(self, operation: Operation) -> bool:
        """确定是否需要进位/借位"""
        if operation in {Operation.ADD, Operation.SUB}:
            return random.random() < self.config.add_sub_carry_ratio
        elif operation == Operation.MUL:
            if self.config.multiplication_table_only:
                return False
            return random.random() < self.config.mul_carry_ratio
        return False

    def _generate_single_question(self, number: int) -> Question:
        """生成单个题目"""
        operation = self._determine_operation()
        need_carry = self._determine_carry_need(operation)

        if operation == Operation.ADD:
            a, b, c = self._generate_addition(need_carry)
        elif operation == Operation.SUB:
            a, b, c = self._generate_subtraction(need_carry)
        elif operation == Operation.MUL:
            a, b, c = self._generate_multiplication(need_carry)
        else:
            a, b, c = self._generate_division()

        blank_position = random.choice(list(BlankPosition))
        return Question(number, a, b, c, operation, blank_position)

    def generate(self) -> List[Question]:
        """生成所有题目"""
        self.questions = [self._generate_single_question(i) for i in range(1, self.config.total_questions + 1)]
        return self.questions

    def format_questions(self) -> str:
        """格式化所有题目"""
        if not self.questions:
            self.generate()

        lines = []
        current_line = []
        separator = ' ' * self.config.spaces_after_question

        for q in self.questions:
            num_str = str(q.number).rjust(self.question_num_width)
            q_content = q.format_question(self.config.blank_underscores, self.num_width)
            question_str = f"{num_str}. {q_content}"
            current_line.append(question_str)

            if len(current_line) >= self.config.questions_per_row:
                lines.append(separator.join(current_line))
                current_line = []

        if current_line:
            lines.append(separator.join(current_line))

        return '\n'.join(lines)

    def format_answers(self) -> str:
        """格式化所有答案"""
        if not self.questions:
            self.generate()

        lines = []
        current_line = []
        answers_per_row = self.config.questions_per_row * 2

        for q in self.questions:
            num_str = str(q.number).rjust(self.question_num_width)
            ans_str = q.format_answer(self.num_width)
            answer_str = f"{num_str}. {ans_str}"
            current_line.append(answer_str)

            if len(current_line) >= answers_per_row:
                lines.append('  '.join(current_line))
                current_line = []

        if current_line:
            lines.append('  '.join(current_line))

        return '\n'.join(lines)

    def get_full_output(self, title: str = "算术练习题") -> str:
        """获取完整输出"""
        ops_names = {Operation.ADD: '加法', Operation.SUB: '减法',
                     Operation.MUL: '乘法', Operation.DIV: '除法'}
        ops_str = '、'.join([ops_names[op] for op in self.config.operations])

        config_info = [
            f"题数: {self.config.total_questions}",
            f"范围: {self.config.min_value}~{self.config.max_value}",
            f"运算: {ops_str}",
        ]

        add_sub_ops = {op for op in self.config.operations if op in {Operation.ADD, Operation.SUB}}
        mul_div_ops = {op for op in self.config.operations if op in {Operation.MUL, Operation.DIV}}

        if add_sub_ops:
            config_info.append(f"加减进位: {self.config.add_sub_carry_ratio * 100:.0f}%")
        if Operation.MUL in self.config.operations and not self.config.multiplication_table_only:
            config_info.append(f"乘法进位: {self.config.mul_carry_ratio * 100:.0f}%")
        if add_sub_ops and mul_div_ops:
            config_info.append(f"加减占比: {self.config.add_sub_group_ratio * 100:.0f}%")
        if self.config.multiplication_table_only and Operation.MUL in self.config.operations:
            config_info.append("乘法: 仅9×9")

        output = [
            "=" * 70,
            title.center(70),
            "=" * 70,
            " | ".join(config_info),
            "=" * 70,
            "",
            self.format_questions(),
            "",
            "=" * 70,
            "答案".center(70),
            "=" * 70,
            "",
            self.format_answers(),
            "",
            "=" * 70,
        ]
        return '\n'.join(output)

    def save_to_file(self, filename: str, title: str = "算术练习题"):
        """保存到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.get_full_output(title))
        print(f"已保存到文件: {filename}")


def main():
    """主函数演示"""

    # 示例1: 简单使用（默认参数）
    # print("【示例1】简单使用 - 20道加减法")
    # print("-" * 70)
    # config1 = QuizConfig(
    #     total_questions=20,
    #     operations={Operation.ADD, Operation.SUB},
    #     max_value=100
    # )
    # gen1 = ArithmeticQuizGenerator(config1)
    # print(gen1.get_full_output("加减法练习"))

    print("\n" + "=" * 70 + "\n")

    # 示例2: 全参数示例
    print("【示例2】全参数配置示例")
    print("-" * 70)
    config2 = QuizConfig(
        total_questions=1000,              # 总题数
        questions_per_row=4,             # 每行4题
        spaces_after_question=1,         # 题目间2个空格
        blank_underscores=2,             # 2个下划线
        num_align_width=2,               # 按2位数对齐
        operations={Operation.ADD, Operation.SUB, Operation.MUL},  # 四则运算
        min_value=0,                     # 最小值0
        max_value=100,                   # 最大值100
        multiplication_table_only=True, # 乘法不限于9×9
        add_sub_carry_ratio=0.5,         # 加减法50%进位
        mul_carry_ratio=0.6,             # 乘法60%进位（9×9以外）
        add_sub_group_ratio=0.8,         # 加减法占80%，乘除法占20%
    )
    gen2 = ArithmeticQuizGenerator(config2)
    print(gen2.get_full_output("四则运算综合练习"))

    # 保存到文件
    gen2.save_to_file("arithmetic_quiz.txt", "四则运算综合练习")


if __name__ == "__main__":
    main()