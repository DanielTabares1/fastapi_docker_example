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