from PIL import Image

flag = True
temp = False
a = int(input("Выберите кота(хотите выйти введите 0)? - 1)белый 2)серый 3)чёрный 4)рыжий = "))

while True:
    if a == 1 or a==2 or a==3 or a==4:
        Img = Image.open("kot_{}.jpg".format(a))
        Img.show()
        temp = int(input('Введите 1 если хотите другого кота,0 если нет = '))
        if temp:
            a = int(input("Выберите кота? - 1)белый 2)серый 3)чёрный 4)рыжий = "))
        else:
            break
    else:
        print("Нет! Такого котика нет! Сейчас отправлю вас назад!")
        a = int(input("Выберите кота(хотите выйти введите 0)? - 1)белый 2)серый 3)чёрный 4)рыжий = "))
    
    
Img.show()

