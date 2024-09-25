from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.users import get_all_users
from src.schemas.users import UserRead
from src.models import db_helper

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await get_all_users(session=session)
    return users
