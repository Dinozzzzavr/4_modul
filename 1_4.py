import json
file = open('example.json','r', encoding='utf-8')
example_data = json.load(file)
if example_data['isFullDay'] == True and len(example_data['language']) >=2:
    print("Проходит на 1 этап")
else:
    print("Не проходит на 1 этап")