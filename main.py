from typing import List, Optional
from uuid import uuid4
from models.models import Item
from fastapi import FastAPI, Query
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Sample Items API",
    version="1.0.0",
    description="Example GET endpoints demonstrating query, path params, and response models",
)

templates = Jinja2Templates(directory="templates")


# In-memory sample data store
items_db: List[Item] = [
    Item(
        id=uuid4(),
        name="Widget",
        description="A useful widget",
        price=9.99,
        tags=["tools", "home"],
    ),
    Item(
        id=uuid4(),
        name="Gadget",
        description="A fancy gadget",
        price=19.99,
        tags=["electronics"],
    ),
    Item(id=uuid4(), name="Thingamajig", description=None, price=4.5, tags=[]),
]


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Hello from AWS ECS Fargate!"}


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


@app.get("/items", response_model=List[Item], tags=["items"])
def list_items(
    q: Optional[str] = Query(None, description="Search term to filter items"),
    skip: int = 0,
    limit: int = 10,
):
    """Return a paginated list of items. Optional `q` filters by name, description or tags."""
    results = items_db
    if q:
        q_lower = q.lower()
        results = [
            item
            for item in results
            if q_lower in item.name.lower()
            or (item.description and q_lower in item.description.lower())
            or any(q_lower in t.lower() for t in item.tags)
        ]
    return results[skip : skip + limit]


@app.get("/donkey", response_class=HTMLResponse)
def read_data(request: Request):
    return templates.TemplateResponse(
        "donkey.html", {"request": request, "message": "You are a donkey!!!"}
    )
