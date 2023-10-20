import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Process a CSV file")
parser.add_argument("C:\Users\18210\Documents\芝加哥汽车超速数据.csv", required=True, help="Path to the CSV file")
parser.add_argument(5, required=True, help="Column number to delete (0-based index)")
args = parser.parse_args()
file_path = args.path
column_to_delete_number = int(args.number)
df = pd.read_csv(file_path)
if column_to_delete_number < len(df.columns):
    df = df.drop(df.columns[column_to_delete_number], axis=1)
new_file_path = "芝加哥汽车超速数据new.csv"
df.to_csv(new_file_path, index=False)
print(f"File '{file_path}' processed. Deleted column number {column_to_delete_number}. Result saved to '{new_file_path}'.")
