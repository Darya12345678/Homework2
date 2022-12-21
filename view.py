import ex1 as c

def dialog_user():
    print('1-просмотр контактов, 2-добавление контакта, 3-поиск контакта по имени/номеру телефона/части номера')
    a = int(input('Введите число: '))
    if a == 1:
        c.contacts()
    if a == 3:
        c.contacts_search()
    elif a == 2:
        c.import_cont() 
    else:
        print('Значение должно быть "1" или "2" без знаков препинания и ковычек')



  
