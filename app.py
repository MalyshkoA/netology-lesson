import time

counter = 0  # счетчик повторений

while True:
    counter += 1
    print(f"Приложение работает. Повторение №{counter}")
    time.sleep(2)  # ожидание 2 секунды
