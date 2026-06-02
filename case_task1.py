cmd = input("Введите команду: ")
match cmd:
    case "start":
        print("Запускаем процесс...")
    case "stop":
        print("Останавливаем процесс...")
    case "restart":
        print("Перезапускаем процесс...")
    case "status":
        print("Процесс работает")
    case _:
        print("Неизвестная команда")
