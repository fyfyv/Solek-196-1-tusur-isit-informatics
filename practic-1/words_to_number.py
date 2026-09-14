def words_to_number(text):
    # объявляю переменные и массивы с которыми буду работать
    wordStr = []
    peaceMass = []
    temp = 0
    result = 0
    # объявляю 2 словаря для того чтобы записат туда как просто числа в духе 2 4 5 так и модификаторы 100 1000 1000000
    numbers = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,"five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9,"ten": 10, 
    "eleven": 11, "twelve": 12,"thirteen": 13,"fourteen": 14, "fifteen": 15, 
    "sixteen": 16, "seventeen": 17,"eighteen": 18, "nineteen": 19,"twenty": 20, 
    "thirty": 30, "forty": 40, "fifty": 50,"sixty": 60, 
    "seventy": 70, "eighty": 80, "ninety": 90,}
    multipliers = {"hundred": 100, "thousand": 1_000, "million": 1_000_000,}
    # убираю мусорные символы вроде "-" а так же "and"
    text = text.replace("-"," ")
    wordStr = text.split()
    for i in range (wordStr.count("and")):  
        wordStr.remove("and")
    # тут мы уже работаем со строкой разбитой на аля "литералы" которые есть в нашем словаре, просто перебираем их все, с индексами не надо работать,
    # если наш литерал из списка "чисел", то просто прибавим и все, если же литерал из списка "мультипликаторов" то смотрим, 
    # если это большой мультпликатор 1000 или 1000000, то умножаем и получившееся число кидаем в массив, цель которого хранить такие вот, сформированные куски,
    # если мультипликатор 100, то перенос не требуется, просто умножаем, во избежании потери данных, после того как мы пройдемся по всем элементам у нас будет кусок,
    # коотрый мы еще не записали в список, делаем это, после чего суммируем куски и записываем в переменную рузультата
    for i in wordStr:
        if i in numbers:
            temp += numbers[i]
        
        elif i in multipliers:
            if i == "thousand" or i == "million":
                temp *= multipliers[i]
                peaceMass.append(temp)
                temp = 0
            
            else:
                temp *= multipliers[i]
    peaceMass.append(temp)

    for i in peaceMass:
        result += i
    return result
if __name__ == "__main__":
# seven hundred eighty-three thousand    nine hundred and nineteen
    print(words_to_number("seven hundred eighty-three thousand nine hundred and nineteen"))