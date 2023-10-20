year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
day = int(input("请输入日期: "))

# 每个月的天数，索引0为占位符，不使用
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 如果是闰年，2月天数加1
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[2] = 29

# 计算本年的第几天
day_count = sum(days_in_month[:month]) + day

print(f"{year}年{month}月{day}日是本年的第{day_count}天")
