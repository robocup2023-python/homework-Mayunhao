import pandas as pd

df = pd.read_csv('芝加哥汽车超速数据.csv') 
column_to_delete = 'date'  
if column_to_delete in df.columns:
    df = df.drop(column_to_delete, axis=1)

# 3. 对某两列执行相加操作
column1 = 'exceeded at night' 
column2 = 'exceeded in daytime' 

if column1 in df.columns and column2 in df.columns:
    df['amount of exceeded'] = df[column1] + df[column2]

# 4. 保存结果到新的 CSV 文件
df.to_csv('new_file.csv', index=False)  # 将结果保存到新的 CSV 文件，可以将 'new_file.csv' 替换为实际的文件路径
