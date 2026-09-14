def days_in_month(month, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year%4==0 and year%100!=0) or year%400==0:
        return 29
    else: return days[month-1]
if __name__ == "__main__":
    print(days_in_month(1, 2001))    # 31
    print(days_in_month(2, 2001))    # 28
    print(days_in_month(2, 2000))    # 29
    print(days_in_month(2, 1900))    # 28
    print(days_in_month(11, 2025))   # 30