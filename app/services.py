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

async def get_user(user_id: int, db: "Session"):
    user = db.query(_models.User).filter(_models.User.id == user_id).first()
    return user

async def delete_user(user: _models.User, db: "Session"):
    db.delete(user)
    db.commit()

async def update_user(user: _models.User, user_data: _schemas.CreateUser, db: "Session") -> _schemas.User:
    user.name = user_data.name
    user.email = user_data.email
    user.image = user_data.image
    user.role = user_data.role
    db.commit()
    db.refresh(user)
    return _schemas.User.from_orm(user)