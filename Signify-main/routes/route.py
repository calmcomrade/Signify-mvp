from fastapi import APIRouter
from models.sign import Sign
from config.database import collection
from schema.schemas import individual_serial
from bson import ObjectId


router = APIRouter()

@router.get('/')
async def get_sign(sign_name):
    sign = individual_serial(collection.find_one({"sign_name": sign_name}))
    return sign

# @router.post('/')
# async def post_sign(sign: Sign):
#     sign_dict = sign.to_dict()
#     collection.insert_one(sign_dict)