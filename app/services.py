from typing import TYPE_CHECKING

import app.database as _database
import app.models as _models
import app.schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_user(user: _schemas.CreateUser, db: "Session") -> _schemas.User:
    user = _models.User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return _schemas.User.from_orm(user)

async def get_users(db: "Session") -> list[_schemas.User]:
    users = db.query(_models.User).all()
    return list(map(_schemas.User.from_orm, users))