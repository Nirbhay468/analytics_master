from repository.crud.base import BaseCRUDRepository
import typing

import fastapi
from sqlalchemy.ext.asyncio import (
    AsyncSession as SQLAlchemyAsyncSession,
)

from repository.session import get_async_session


def get_repository(
    repo_type: typing.Type[BaseCRUDRepository],
) -> typing.Callable[[SQLAlchemyAsyncSession], BaseCRUDRepository]:
    def _get_repo(
        async_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
    ) -> BaseCRUDRepository:
        return repo_type(async_session=async_session)

    return _get_repo