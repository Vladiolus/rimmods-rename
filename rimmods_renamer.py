import os
import re
import xml.etree.ElementTree as ET

print("""
~~~~~~~~~~~~~
ИНИЦИАЛИЗАЦИЯ
~~~~~~~~~~~~~
""")

directory = input("Укажите папку с модами: ")
directory = os.path.normpath(directory)

mods = [mod for mod in os.listdir(directory) if os.path.isdir(os.path.join(directory, mod)) and re.match("^\d", mod)]
list = '\n'.join(map(str, mods))

print(f"\nПереименованы будут следующие моды: \n{list}\n")

print("Запускаем...")
sub_path = "About\About.xml"
for mod in mods:
    mod_path = os.path.join(directory, mod)
    xml_path = os.path.join(mod_path, sub_path)
    if not os.path.exists(xml_path):
        print(f"{mod} не содержит файла {sub_path}")
        continue

    try:
        root = ET.parse(xml_path).getroot()
    except ET.ParseError:
        print(f"{mod}: ошибка при прочтении файла {sub_path}")
        continue
    
    name_field = root.find("name")
    if name_field is None:
        print(f"{mod}: отсутствует информация о названии в файле {sub_path}")
        continue

    mod_name = name_field.text
    clear_name = re.sub(r"[\*\|\\\:\"<>\?\/]", "", mod_name)
    print(f"{mod} -> {clear_name}")

    new_path = os.path.join(directory, clear_name)
    if not os.path.exists(new_path):
        os.rename(mod_path, new_path)

print("""
Операция выполнена.
ДО СКОРОЙ ВСТРЕЧИ.
""")

input("Нажмите Enter чтобы выйти. ")