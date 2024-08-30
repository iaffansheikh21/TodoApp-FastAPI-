
from sqlmodel import SQLModel, Field # type: ignore

class Todos(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    is_completed: bool
    
class Update_Todos(SQLModel):
    
    title: str | None
    description: str | None
    is_completed: bool | None