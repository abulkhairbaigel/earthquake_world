# На карте землетрясений должна быть указана магнитуда каждого из них.
# Мы можем отобразить больше данных, т.к. информация наносится правильно. 

from pathlib import Path
import json

import plotly.express as px

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_30_day_m1.geojson')    # мы загружаем файл с землетрясениями за 30 дней.
# Тут возникала ошибка чтения файла:
contents = path.read_text(encoding='utf-8')
# Эта ошибка возникает из-за того, что ваш файл в формате GeoJSON содержит символы (например, буквы с диакритическими знаками,
# спецсимволы или другой язык), которые не поддерживаются кодировкой по умолчанию в вашей операционной системе.
# Чтобы решить эту проблему, вам нужно явно указать правильную кодировку при чтении файла — чаще всего это utf-8.
all_eq_data = json.loads(contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] 
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = 'Глобальные землетрясения'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title)   # добавлям аргумент size, чтобы изменять размер точек на карте.
# этому аргументу передаем список магнитуд mags.
fig.show()

# Мы можем улучшить карту, меняя цвет точек для обозначения магнитуды.