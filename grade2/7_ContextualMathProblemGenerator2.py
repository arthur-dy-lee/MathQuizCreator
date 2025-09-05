# -*- coding: utf-8 -*-
# @Time   : 5/9/2025 19:52
# @Author : arthur.dy.lee
# @Email  : arthur.dy.lee@gmail.com
# @File   : 7_ContextualMathProblemGenerator2.py
# @Project: MathQuizCreator
import random


class ChineseMathProblemGenerator:
    def __init__(self, num_problems, lines_per_problem=2):
        self.num_problems = num_problems
        self.lines_per_problem = lines_per_problem
        self.problems = []
        self.answers = []

    def generate_problems(self):
        problem_types = [
            self._generate_transfer_problem,
            self._generate_book_problem,
            self._generate_fruit_problem,
            self._generate_age_problem
        ]

        for i in range(self.num_problems):
            # 随机选择一种题型
            problem_func = random.choice(problem_types)
            problem, answer = problem_func(i + 1)

            self.problems.append(problem)
            self.answers.append(answer)

    def _generate_transfer_problem(self, index):
        """生成人员调动类题目"""
        initial = random.randint(15, 40)
        transfer = random.randint(1, 10)
        answer = 2 * transfer

        problem = (
            f"{index}. 学校数学和语文兴趣小组的人数正好相等，都是{initial}人，"
            f"现在如果要从数学小组抽出{transfer}人到语文小组，"
            "那么数学小组比语文小组少了（__）人"
        )
        return problem, answer

    def _generate_book_problem(self, index):
        """生成图书分配类题目"""
        total_books = random.randint(30, 90)
        classes = random.randint(3, 6)
        books_per_class = total_books // classes
        remainder = total_books % classes

        problem = (
            f"{index}. 学校图书馆新购进{total_books}本图书，"
            f"平均分给{classes}个班级，每个班分得（__）本，还剩（__）本"
        )
        answer = f"{books_per_class} {remainder}"
        return problem, answer

    def _generate_fruit_problem(self, index):
        """生成水果分配类题目"""
        apples = random.randint(20, 50)
        oranges = random.randint(10, 40)
        students = random.randint(5, 15)

        total_fruits = apples + oranges
        fruits_per_student = total_fruits // students
        remainder = total_fruits % students

        problem = (
            f"{index}. 老师带来{apples}个苹果和{oranges}个橘子，"
            f"要平均分给{students}个小朋友，每个小朋友分得（__）个水果，还剩（__）个"
        )
        answer = f"{fruits_per_student} {remainder}"
        return problem, answer

    def _generate_age_problem(self, index):
        """生成年龄问题类题目"""
        father_age = random.randint(30, 45)
        son_age = random.randint(5, 15)
        years_later = random.randint(5, 10)

        father_future = father_age + years_later
        son_future = son_age + years_later
        age_difference = father_future - son_future

        problem = (
            f"{index}. 爸爸今年{father_age}岁，儿子今年{son_age}岁。"
            f"{years_later}年后，爸爸比儿子大（__）岁"
        )
        answer = age_difference
        return problem, answer

    def print_problems_and_answers(self):
        # 打印所有题目
        for problem in self.problems:
            print(problem)
            for _ in range(self.lines_per_problem):
                print()

        # 打印答案
        print("\n答案：")
        for i, answer in enumerate(self.answers):
            print(f"{i + 1}. {answer}")


def main():
    # 生成8道题目，每题后空2行
    generator = ChineseMathProblemGenerator(num_problems=8, lines_per_problem=2)
    generator.generate_problems()
    generator.print_problems_and_answers()


if __name__ == "__main__":
    main()