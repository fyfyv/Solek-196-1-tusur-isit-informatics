def century_message(name, age, current_year):
    return f"{name}, тебе исполнится 100 лет в {current_year - age + 100} году"
if __name__ == "__main__":
    century_message("Аня", 20, 2025)   # 'Аня, тебе исполнится 100 лет в 2105 году'