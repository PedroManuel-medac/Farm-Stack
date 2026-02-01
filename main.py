from fastapi import FastAPI
from database import get_all_tasks #importamos la función
from models import Task

app = FastAPI()


#Esto se ejecutará cuando se abra la web
@app.get('/')
def welcome():
    return 'Backend funcionando'

#Aqui llamamos a la función de database 'get_all_tasks()'
@app.get('/api/tasks')
async def get_tasks():
    task = await get_all_tasks()
    return task

#ME HE QUEDADO POR AQUÍ
@app.post('/api/tasks')
async def create_tasks():
    return 'Creando tarea'

@app.get('/api/tasks/{id}')
async def get_tasks_id():
    return 'Devolviendo tarea por id'

@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'Actualizando tarea'

@app.delete('/api/tasks/{id}')
async def delete_tasks():
    return 'Eliminando tarea'