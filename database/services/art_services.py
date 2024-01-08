from ..models.user_model import User, users_collection
from ..models.art_model import Art, arts_collection


async def get_arts() -> list[Art]:
    arts = arts_collection.find()
    return [Art(**a) async for a in arts]


async def get_art_by_username(username: str) -> list[Art]:
    arts =  arts_collection.find({'creator': username})
    return [Art(**a) async for a in arts]

async def get_art_by_id(id: str) -> Art or None:
    art = await arts_collection.find_one({'_id': id})
    return Art(**art) if art else None

async def get_art_by_artist(user: str) -> list[Art] or None:
    # Find all users with the given name
    users_with_curr_name = await users_collection.find({'name': user}).to_list(length=None)

    if users_with_curr_name:
        # Get all user_names from the list of users
        user_names = [u['user_name'] for u in users_with_curr_name]

        # Find arts based on the list of user_names
        arts_cursor = arts_collection.find({'creator': {'$in': user_names}})

        # Convert the cursor to a list of dictionaries
       

        # Return the list of arts
        return [Art(**a) async for a in arts_cursor]

    # Return None if no users are found with the given name
    return None

async def get_art_by_tag(tag: str) -> list[Art] or None:
    arts = arts_collection.find({'tag': tag})
    return [Art(**a) async for a in arts]


async def create_art(**kwargs) -> list[Art]:
    art = await arts_collection.insert_one({**kwargs})
    return await get_art_by_id(art.inserted_id)


async def update_art_by_id(id: str, **kwargs) -> Art:
    art = await arts_collection.find_one_and_update({'_id': id}, {'$set': kwargs}, return_document=True)
    return Art(**art)
