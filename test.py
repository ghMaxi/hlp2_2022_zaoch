try:
    raise ValueError("Я не Вася")
    a = a / 0
except ZeroDivisionError:
    print("Делить на 0 нельзя!")
except ValueError:
    print("Вася не число!")

print("Программа завершилась штатно")