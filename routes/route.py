from fastapi import APIRouter
from models.todo import Todo
from config.database import collection_name
from schema.schemas import list_serializer
from bson import ObjectId

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_todo_list():
    todo_list = list_serializer(collection_name.find())

    return todo_list

# POST Request Method
@router.post("/")
async def post_todo(item: Todo):
    collection_name.insert_one(dict(item))

# PUT Request Method
@router.put("/{id}")
async def put_todo(id: str, item: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(item)})

# DELETE Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})