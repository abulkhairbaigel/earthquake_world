# Данные о местоположении хранятся с ключом "geometry". В словаре "geometry" есть ключ "coordinates",
# первыми двумя значениями которого являются долгота и широта.

from pathlib import Path
import json

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []    # создаются списки для долгот и широт.
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    # eq_dict['geometry'] обращается к словарю, представляющему элемент geometry данных землетрясения.
    # второй ключ 'coordinates' извлекает список значений, связанных с ключом 'coordinates'.
    # наконец индекс 0(или 1) запрашивает первое(или второе) значение в списке координат.
    lon = eq_dict['geometry']['coordinates'][0] 
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Имея эти данные можно переходить к их нанесению на карту.