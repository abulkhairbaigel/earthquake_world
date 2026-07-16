# Начнем с создания списка, содержащего всю информацию обо всех произошедших землетрясениях.

from pathlib import Path
import json

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('создание карт с глобальными наборами данных формат geojson/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Берем данные, связанные с ключом 'features', и сохраняем их в all_eq_data.
# Известно, что файл содержит данные 160 землетрясений.

# Далее, мы извлечем данные магнитуд по каждому землетрясению. 