import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from views import tic_home

api = fastapi.FastAPI()


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(tic_home.router)


if __name__ == '__main__':
    configure_routing()
    uvicorn.run(api)
else:
    configure_routing()