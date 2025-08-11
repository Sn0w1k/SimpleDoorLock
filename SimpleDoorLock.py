password = int(input('Введите новий пароль: '))
count = 3

def guess_password(count):
    while count > 0:
        admin = input('Введите пароль: ')
        if not admin.isdigit():
            print("Пароль должен содержаться только из цифр")
            continue
        if int(admin) == password:
            return 'Пароль вірний!'
        count -= 1
        print("Пароль неправильний!")
        if count == 0:
            return "всі 3 спроби вичерпані!"
    
result = guess_password(count)
print(result)