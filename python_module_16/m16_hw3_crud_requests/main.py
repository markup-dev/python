from fastapi import FastAPI, Body, status, HTTPException, Request, Path
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
	id: int = None
	username: str = None
	age: int = None


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
	return templates.TemplateResponse('users.html', context={'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
	return templates.TemplateResponse('users.html', context={'request': request, 'user': users[user_id-1]})


@app.post('/user/{username}/{age}')
async def post_user(
		username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
		age: Annotated[int, Path(gt=18, le=120, description='Enter age', example=22)]) -> str:
	user_id = len(users) + 1
	user = User(id=user_id, username=username, age=age)
	users.append(user)
	return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
		user_id: Annotated[str, Path(description='Enter user id', example='1')],
		username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
		age: Annotated[int, Path(gt=18, le=120, description='Enter age', example=22)]) -> str:
	try:
		edit_user = users[int(user_id) - 1]
		edit_user.username = username
		edit_user.age = age
		return f'User {user_id} has been updated'
	except IndexError:
		raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(description='Enter user id', example='1')]) -> object:
	try:
		deleted_user = users.pop(int(user_id) - 1)
		return deleted_user
	except IndexError:
		raise HTTPException(status_code=404, detail="User was not found")
