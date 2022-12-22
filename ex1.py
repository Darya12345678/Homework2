def contacts():
 base = {}
 with open (r'tel1.txt', encoding ='utf-8') as f:
      for line in f:
         key,val = line.strip().split(':')
         base[key] = val.split()
 for key,val in base.items():
     print(f"{key} : {' '.join(val)}")

# contacts()


def import_cont():
  with open ('tel1.txt','a', encoding="utf-8" ) as n:
           text_name = input('Введите ФИО ')
           text_numb = input('Введите телефон')
           text = str(f'{text_name} : тел. {text_numb}')
           n.write('\n')
           for line in text:
                 n.write(line)
           
# import_cont()           

def contacts_search():
 name = str(input('Введите номер телефона или часть номера контакта: '))
 with open (r'tel1.txt', encoding ='utf-8') as f:
      for line in f:
         if name in str(line):
            print(line)
            from datetime import datetime as dt
            time = dt.now().strftime('%H:%M')
            with open ('log.csv','a', encoding="utf-8") as file:
                file.write('{};{}'.format(time,line))

# contacts_search()


