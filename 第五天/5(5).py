import os
import random
import string

current_directory = os.path.dirname(os.path.abspath(__file))

img_directory = os.path.join(current_directory, 'img')
os.makedirs(img_directory, exist_ok=True)

for i in range(100):
    random_suffix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    if i < 50:
        file_name = f'X{random_suffix}.jpg'
    else:
        file_name = f'X{random_suffix}.png'
    file_path = os.path.join(img_directory, file_name)

    with open(file_path, 'w'):
        pass

print("目录 'img' 已创建，并包含100个文件，其中50个文件的结尾已改为jpg。")
