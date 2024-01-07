from ..models.user_model import User, users_collection
from ..models.art_model import Art, arts_collection


async def get_arts() -> list[Art]:
    arts = arts_collection.find()
    return [Art(**a) async for a in arts]


async def get_art_by_username(username: str) -> Art or None:
    art = await arts_collection.find_one({'user_name': username})
    return Art(**art) if art else None

async def get_art_by_user(user: str) -> Art or None:
    usernames =  await users_collection.find({'name': user})

    arts =[await arts_collection.find({'user_name': username}) for username in usernames]
    return [Art(**a) async for a in arts]

async def get_art_by_tag(tag: str) -> Art or None:
    arts = await arts_collection.find_one({'tag': tag})
    return [Art(**a) async for a in arts]


async def create_art(**kwargs) -> Art:
    art = await arts_collection.insert_one({**kwargs})
    return await get_art_by_id(art._id)


async def update_art_by_id(id: int, **kwargs) -> Art:
    art = await arts_collection.find_one_and_update({'_id': id}, {'$set': kwargs}, return_document=True)
    return Art(**art)
