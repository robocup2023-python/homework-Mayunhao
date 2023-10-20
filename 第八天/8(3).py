import os
import random
import string

# 创建名为 "img" 的目录
os.makedirs("img", exist_ok=True)

# 生成 100 个不同的文件名
for i in range(100):
    # 生成随机的文件名，例如 X4G5.png
    file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) + '.png'
    
    # 使用 open 函数创建文件并写入内容
    with open(os.path.join("img", file_name), 'w') as file:
        file.write("This is file number {}".format(i + 1))

print("已创建 100 个不同的文件。")
