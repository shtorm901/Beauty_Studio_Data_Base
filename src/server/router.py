from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.Client, database_model=database_models.Client, prefix='/clients', tags=['Clients']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Post, database_model=database_models.Post, prefix='/posts', tags=['Posts']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Services, database_model=database_models.Services, prefix='/services', tags=['Services']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Visits, database_model=database_models.Visits, prefix='/visits', tags=['Visits']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Workers, database_model=database_models.Workers, prefix='/workers', tags=['Workers']).fastapi_router
)
