# Чтобы закончить создание карты, мы добавим подсказку, которая будет появляться при наведении указателя мыши на маркер, обозначающий землетрясение.
# Помимо вывода долготы и широты, мы выведем магнитуду и описание приблизительного местоположения.

from pathlib import Path
import json

import plotly.express as px

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []   # сначла создаем новый список для хранения названий всех землетрясений.
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] 
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']    # из ключа title извлекается название и передается переменной eq_title.
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)   # переменную добавляем к списку.

title = 'Глобальные землетрясения'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='ylorrd',
                     labels={'color': 'Магнитуда'},
                     projection='natural earth',
                     hover_name=eq_titles    # теперь plotly добавит инфо о каждом землетрясении в текст подсказки для каждой точки.
                     )
fig.show()

