from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
'''
__file__ - полный путь к файлу где написан этот код
.parent(1) - расширяет обзор до папки, где лежит файл с кодом
.parent(2) - на 1 директорию выше папки с кодом

Очень странно, что этот путь не идёт дальше по коду.
Ибо в файле с конфигом пришлось сделать то же самое, что бы переменные из .env начали подвязываться

P.S. в файле конфига Pydentic смотрит на директорию вызова -> src | os.getcwd()
Пришлось прогнутся и скопировать Path(__file__).parent.parent
'''

from src.api.route_hotels import router as router_hotels
from src.config import settings


app = FastAPI() # Главный обьект, без него не как
app.include_router(router_hotels) # Роутинг на отдельные маршруты | Деление трансопрта
templates = Jinja2Templates(directory='templates') # html Вёрстка


hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'voc'},
    {'id': 2, 'title': 'Dubai', 'name': 'bok'},
]

# Корневой маршрут
@app.get('/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request}) # Маршрут для html


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)