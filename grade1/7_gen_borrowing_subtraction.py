import random

class SubtractionProblemGenerator:
    # 20以内借位减法题生成器

    def __init__(self, num_problems=500, a_range=(11,20), b_range=(2,9), per_row=4):
        self.num_problems = num_problems
        self.a_min, self.a_max = a_range
        self.b_min, self.b_max = b_range
        self.per_row = per_row
        
    def _generate_problem(self):
        """生成单个符合借位条件的减法题"""
        while True:
            a = random.randint(self.a_min, self.a_max)
            b = random.randint(self.b_min, self.b_max)
            if b > (a % 10): 
                return f"{a} - {b} = "
    
    def generate(self):
        """生成带行号的格式化输出"""
        problems = [self._generate_problem() for _ in range(self.num_problems)]
        
        grouped = [
            problems[i:i+self.per_row] 
            for i in range(0, len(problems), self.per_row)
        ]
        
        return '\n\n'.join(
            f"({i+1})  {'           '.join(row)}"
            for i, row in enumerate(grouped)
        )

if __name__ == "__main__":
    generator = SubtractionProblemGenerator()
    print(generator.generate())