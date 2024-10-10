import io

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')  #  открываем и декодируем файл
    strings_positions = {}                         # создаем словарь
    str_num = 0
    str_start_byte = file.seek(0)

    for i in strings:
        file.write(i+'\n')
        str_num += 1
        key = (str_num, str_start_byte)
        strings_positions[key] = i
        str_start_byte = file.tell()
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('file_name.txt', info)
for elem in result.items():
  print(elem)
