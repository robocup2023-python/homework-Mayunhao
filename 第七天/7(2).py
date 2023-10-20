import random
import string
import shutil
def generate_and_copy_file(num_lines):

    with open('test.txt', 'w') as file:
        for _ in range(num_lines):
            line = ''.join(random.choice(string.printable) for _ in range(80))
            file.write(line + '\n')

    shutil.copy('test.txt', 'copy_test.txt')
num_lines = int(input("请输入行数: "))
generate_and_copy_file(num_lines)
print(f"{num_lines} 行内容已生成并拷贝为 'copy_test.txt'。")
