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



