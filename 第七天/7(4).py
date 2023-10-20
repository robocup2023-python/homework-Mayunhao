def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    different_lines = []
    for i, (line1, line2) in enumerate(zip(lines1, lines2)):
        if line1 != line2:
            different_lines.append(i + 1)

    return different_lines

# 比较 'test.txt' 和 'copy_test.txt' 的内容
different_lines = compare_files('test.txt', 'copy_test.txt')

if different_lines:
    print("以下行在两个文件中不同:")
    print(different_lines)
else:
    print("两个文件内容完全相同.")
