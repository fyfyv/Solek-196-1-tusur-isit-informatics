def month_calendar(start_weekday, days):
    weekls = []
    result = []

    for i in range(start_weekday):
        weekls.append("  ")
    
    for j in range(1,days + 1):
        # if len(str(j)) == 2:
        #     weekls.append(str(j))
        # else: weekls.append(f" {str(j)}")
        # это первая версия выравнивания по правому краю, я изначально требование на сайте проглядел
        weekls.append(f"{j:2}")

    for t in range(0,len(weekls),7):
        result.append(weekls[t:t+7])
    
    resultStr = ""
    for i in result:
        resultStr += " ".join(i) + "\n"
    resultStr = resultStr.rstrip()
    return resultStr
if __name__ == "__main__":
    print(month_calendar(6, 31))