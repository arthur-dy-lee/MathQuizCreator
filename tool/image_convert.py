"""
@Author: arthur
@Email: arthur.dy.lee@gmail.com
@Date: 3/4/2025 5:52 PM
@Last Modified by: arthur
@Last Modified time: 3/4/2025 5:52 PM
"""
from PIL import Image
import os
import sys


class ImageConvert:
    """
    一个用于图像格式转换的类，支持将 WebP 转换为 PNG。
    """

    def __init__(self, input_path: str):
        self.input_path = input_path
        self.output_path = self._generate_output_path()

    def _generate_output_path(self):
        """生成 PNG 输出文件路径，保持与输入文件一致"""
        base, _ = os.path.splitext(self.input_path)
        return f"{base}.png"

    def convert_webp_to_png(self):
        """执行 WebP 到 PNG 的转换"""
        try:
            with Image.open(self.input_path) as img:
                img.save(self.output_path, "PNG")
            print(f"转换成功: {self.input_path} -> {self.output_path}")
        except Exception as e:
            print(f"转换失败: {e}")


if __name__ == "__main__":

    input_file = 'F:\\AI头像\\千万个为什么.webp'
    if not os.path.exists(input_file):
        print("文件不存在，请检查路径。")
        sys.exit(1)

    converter = ImageConvert(input_file)
    converter.convert_webp_to_png()