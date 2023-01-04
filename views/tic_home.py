
import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from calculations import tictactoe
from models.responses import UserResponse, AppResponse

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get("/tictactoe")
def tic_get(request: Request):
    response = AppResponse()
    result = tictactoe.return_board(response)
    return templates.TemplateResponse("tic_index.html", {'request': request, 'result': result})


@router.put("/tictactoe")
def tic_put(response: UserResponse):
    result = tictactoe.playgame(response)
    return result


