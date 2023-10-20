with open('test.txt', 'r') as file:
    file_content = file.read()

# 在文件开头和结尾追加字符串
file_content = "python" + file_content + "python"

# 写回到文件
with open('test.txt', 'w') as file:
    file.write(file_content)

print("文件 'test.txt' 已在开头和结尾追加字符串 'python'。")
这个程序首先打开文件 test.txt 并读
