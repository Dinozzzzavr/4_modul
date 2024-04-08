# Парсинг JSON-документа

# ключи в JSON - строки.
# значениями в JSON могут быть:
    # число (целое или вещественное)
    # true («истина»), false («ложь»), null (отсутствие значения)
    # строка (набор символов внутри двойных кавычек)
    # список (набор элементов внутри квадратных скобок)
    # запись (набор пар ключ: значение внутри фигурных скобок)
import json

human = {
    'name': 'Дима',
    'age': 18,
    'city': 'Москва'
}
human_json = json.dumps(human,ensure_ascii=False)
print(human_json)
print(type(human_json))
file = open('human.json','w')
json.dump(human,file,ensure_ascii=False,indent=4)


