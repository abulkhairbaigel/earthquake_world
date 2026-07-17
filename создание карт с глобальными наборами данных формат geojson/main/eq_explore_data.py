# С помощью plotly мы ожем настроить цвет каждого маркера в зависимости от магнитуды соответствующего землетрясения.
# Мы также изменим проекцию для самой карты. 

from pathlib import Path
import json

import plotly.express as px

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
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
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='peach',     # тут я изменил цвет.
                     labels={'color': 'Магнитуда'},
                     projection='natural earth',
                     )
# Все существенные изменения вносятся в вызов функции px.scatter_geo().
# Аргумент color определяет, какие значения цветовой шкалы следует использовать для окрашивания каждого маркера.
# Мы используем список mags для определения цвета каждой точки, как в случае с аргументом size.

# color_continuous_scale ссылается на используемую цветовую шкалу. 'Viridis' это цветовая шкала с оттенками от синего до желтого.
# По умолчанию цветовая шкала сопровождается меткой color. Аргумент labels принимает словарь в качестве значения.
# Нам нужна только одна пользовательская метка на нашей карте, чтобы цветовая шкала обозначалась по другому.

# Аргумент projection принимает одну из распространенных картографических проекций.
# Мы используем проекцию 'natural earth', которая округляет края карты.
fig.show()

