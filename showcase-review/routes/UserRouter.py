from fastapi import APIRouter, Depends, HTTPException



Router = APIRouter()


@Router.get('/users')
async def get_user():
    return 'user'