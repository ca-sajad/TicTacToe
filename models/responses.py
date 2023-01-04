from pydantic import BaseModel


class Button(BaseModel):
    button: int        # button0_0: 0, button0_1: 1, ..., button2_2: 8
    choice: str        # "O" or "X"


class AppResponse(BaseModel):
    buttons = []
    for i in range(9):
        buttons.append(Button(button=i, choice=""))
    winner: str = ""


class UserResponse(BaseModel):
    changed_button: str         # button0, button1, ..., button8
    changed_choice: str         # "O" or "X"
    difficulty: str             # "easy" or "hard"
    restart: str                # "True" or "False"

