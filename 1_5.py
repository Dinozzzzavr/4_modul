import json
file = open("countries_languages.json")
date = json.load(file)
languages_dict = {}
for item in date:
    languages = item['language']
    country = item['country']
    languages_dict[languages] = country
print("Введите язык")
language = input()
if language not in languages_dict.keys():
        print("отсутствует")
        languages_dict[language] = "Россия"
print(languages_dict)
new_date ={
    'contry':f"{country}",
    'language':f"{language}",
}