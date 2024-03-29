from ..models.user_model import User, users_collection


async def get_users() -> list[User]:
    users = users_collection.find()
    return [User(**u) async for u in users]


async def get_user_by_id(id: str) -> User or None:
    user = await users_collection.find_one({'_id': id})
    return User(**user) if user else None

async def get_user_by_username(username: str) -> User or None:
    user = await users_collection.find_one({'user_name': username})
    return User(**user) if user else None

async def get_user_by_name(name: str) -> list[User]:
    users = users_collection.find({'name': name})
    return [User(**u) async for u in users]


async def create_user(**kwargs) -> User:
    user = await users_collection.insert_one({**kwargs})
    return await get_user_by_id(user.inserted_id)


async def update_user(id: str, **kwargs) -> User:
    user = await users_collection.find_one_and_update({'_id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)
