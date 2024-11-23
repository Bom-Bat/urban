from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import *
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix="/user", tags=["user"])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    return db.scalars(select(User)).all()


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)],
                     user_id: int):
    user_ = db.scalar(select(User).where(user_id == User.id))
    if user_ is None:
        raise HTTPException(status_code=404,
                            detail='User was not found')
    return user_


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)],
                      create_user_: CreateUser):
    user_ = db.scalar(select(User).where(create_user_.username == User.username))
    if user_ is not None:
        raise HTTPException(status_code=400,
                            detail='User already exists')
    db.execute(insert(User).values(username=create_user_.username,
                                   firstname=create_user_.firstname,
                                   lastname=create_user_.lastname,
                                   age=create_user_.age,
                                   slug=slugify(create_user_.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)],
                      update_user_: UpdateUser,
                      user_id: int):
    user_ = db.scalar(select(User).where(user_id == User.id))
    if user_ is None:
        raise HTTPException(status_code=404,
                            detail='User was not found')
    db.execute(update(User).where(user_id == User.id).values(firstname=update_user_.firstname,
                                                             lastname=update_user_.lastname,
                                                             age=update_user_.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User update is successful!'}



@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)],
                      user_id: int):
    user_ = db.scalar(select(User).where(user_id == User.id))
    if user_ is None:
        raise HTTPException(status_code=404,
                            detail='User was not found')

    db.execute(delete(User).where(user_id == User.id))
    db.execute(delete(Task).where(user_id == Task.user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User delete is successful!'}


@router.get('/user_id/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)],
                           user_id: int):
    user_ = db.scalar(select(User).where(user_id == User.id))
    if user_ is None:
        raise HTTPException(status_code=404,
                            detail='User was not found')
    return db.scalars(select(Task).where(user_id == Task.user_id)).all()