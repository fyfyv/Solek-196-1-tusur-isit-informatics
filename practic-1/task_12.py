def shortest_distance(kilometers, meters):
    return min(int(kilometers*1000),meters)
if __name__ == "__main__":
    shortest_distance(1, 500)    # 500   (1 км = 1000 м, значит 500 м меньше)
    shortest_distance(0.2, 900)  # 200
    shortest_distance(1, 1000)   # 1000  (равны - возвращаем это значение)