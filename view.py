import ex1 as c

def dialog_user():
    print('1-просмотр контактов, 2-добавление контакта')
    a = int(input('Введите число: '))
    if a == 1:
        c.contacts()
    elif a == 2:
        c.import_cont() 
    else:
        print('Значение должно быть "1" или "2" без знаков препинания и ковычек')



  
