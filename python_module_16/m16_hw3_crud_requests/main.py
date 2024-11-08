from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
	id: int = None
	username: str = None
	age: int = None


@app.get('/users/')
async def get_all_users() -> List[User]:
	return users


@app.post('/user/{username}/{age}')
async def post_user(
		username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
		age: Annotated[int, Path(gt=18, le=120, description='Enter age', example=22)]) -> str:
	new_user_id = len(users) + 1
	user = User(id=new_user_id, username=username, age=age)
	users.append(user)
	return f'User {new_user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
		user_id: Annotated[str, Path(description='Enter user id', example='1')],
		username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
		age: Annotated[int, Path(gt=18, le=120, description='Enter age', example=22)]) -> str:
	try:
		edit_user = users[int(user_id)-1]
		edit_user.username = username
		edit_user.age = age
		return f'User {user_id} has been updated'
	except IndexError:
		raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(description='Enter user id', example='1')]) -> object:
	try:
		deleted_user = users.pop(int(user_id)-1)
		return deleted_user
	except IndexError:
		raise HTTPException(status_code=404, detail="User was not found")
