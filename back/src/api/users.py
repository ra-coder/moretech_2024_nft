from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import aggregate_order_by

from db.connect import AsyncSessionLocal, get_async_db_session
from db import User, Wallet

users_search_router = APIRouter()


class WalletInfo(BaseModel):
    id: int
    address: str
    is_confirmed: bool


class UserInfo(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    wallets: list[WalletInfo]


class UsersInfo(BaseModel):
    users: list[UserInfo] = []


@users_search_router.post("/api/users/search", response_model=UsersInfo)
async def users_search(
    async_db_session: AsyncSessionLocal = Depends(get_async_db_session),
) -> UsersInfo:
    query = select(

        aggregate_order_by(
            func.jsonb_build_object(
                'id', User.id,
                'email', User.email,
                'first_name', User.first_name,
                'last_name', User.last_name,
                'wallets', func.array_agg(
                    func.jsonb_build_object(
                        'id', Wallet.id,
                        'address', Wallet.address,
                        'is_confirmed', Wallet.is_confirmed
                    )
                )
            ),
            User.last_name,
            User.first_name,
        )
    ).select_from(
        User,
    ).join(
        Wallet,
        Wallet.user_id == User.id,
        is_outer=True,
    )
    result = await async_db_session.execute(query)
    return UsersInfo(users=result.scalars())
