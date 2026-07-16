# Имея список, содержащий данные по всем землетрясениям, мы можем перебрать содержимое списка и извлечь его.
# В нашем случае это магнитуда. 

from pathlib import Path
import json

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']

mags = []    # создадим список для магнитуд.
for eq_dict in all_eq_dicts:      # переберем в цикле словарь all_eq_dicts.
    # Внутри цикла каждое землетрясение представляется словарем eq_dict.
    mag = eq_dict['properties']['mag']     # магнитуда каждого землетряс. хранится в секции 'properties' словаря с ключом 'mag'.
    mags.append(mag)

print(mags[:10])   # выведем первые 10 магнитуд.


# Далее мы извлечем данные координат для каждого землетрясения.