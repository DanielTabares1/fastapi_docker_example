from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import app.schemas as _schemas
import sqlalchemy.orm as _orm
import app.services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/users/", response_model=_schemas.User)
async def create_user(
    user: _schemas.CreateUser, 
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_user(user, db)

@app.get("/api/users/", response_model=List[_schemas.User])
async def get_users(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_users(db)

@app.get("/api/users/{user_id}/", response_model=_schemas.User)
async def get_user(
    user_id: int, 
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    user = await _services.get_user(user_id = user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/api/users/{user_id}/")
async def delete_user(
    user_id: int, 
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User not found")
    await _services.delete_user(user, db=db)
    return "Succesfully deleted user"