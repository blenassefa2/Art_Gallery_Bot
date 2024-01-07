from aiogram.fsm.state import StatesGroup, State

class User(StatesGroup):
    name = State()
    user_name = State()
    photo = State()


class Art(StatesGroup):
    creator = State()
    tag = State()
    image = State()
    
    