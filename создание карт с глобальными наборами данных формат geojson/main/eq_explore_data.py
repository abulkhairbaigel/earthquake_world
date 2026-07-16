# На основании всей информации можно создать простую карту мира.
# И хотя первая версия будет выглядеть довольно простой, нужно убедиться в том, что
# информация отображается правильно, прежде чем сосредоточиться на стиле и визульном оформлении.   

from pathlib import Path
import json

import plotly.express as px    # импортируем модуль plotly.express под псевдонимом px

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
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
fig = px.scatter_geo(lat=lats, lon=lons, title=title)   # функция scatter_geo() позволяет изложить на карту диаграмму разброса географических данных.
# В простейшем варианте диаграмму нам нужно предоставить лишь список шиорт и долгот.
fig.show()