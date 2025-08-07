from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from route_hotels import router as router_hotels


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