from motor.motor_asyncio import AsyncIOMotorClient
from models import Task

cliente = AsyncIOMotorClient('mongodb://adminRoot:pedro@localhost:27017') #Conexión con mongodb
database = cliente.taskdatabase #Creamos la base de datos
collection = database.tasks #Creamos la coleccion

#Esta función obtendrá la tarea del id que le pasas
async def get_one_task_id(id):
    task = await collection.find_one({'_id': id})
    return task

#Esta función creará la tarea que le pasas
async def create_task(task):
    new_task = await collection.insert_one(task)
    create_task = await collection.find_one({'_id': new_task.inserted_id})
    return create_task

#Esta función mostrará todas las tareas usando un cursor
async def get_all_tasks():
    tasks = []
    cursor = await collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks 

#Esta función actualizará la tarea que le pasas
async def update_task(id: str, task):
    await collection.update_one({'_id': id}, {'$set': task})
    document = await collection.find_one({'_id': id})
    return document

#Esta tarea elimina la tarea que le pasas (id)
async def delete_task(id: str):
    await collection.delete_one({'_id': id})
    return True
     