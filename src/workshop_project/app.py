from fastapi import FastAPI

from .api import router

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'operations',
        'description': 'Создание, редактирование, удаление и просмотр операций',
    },
    {
        'name': 'reports',
        'description': 'Импорт и экспорт CSV-отчетов',
    },
]

app = FastAPI(
    title='workshop',
    description='Bla bla description',
    version='1.2.1',
    openapi_tags=tags_metadata,
)
app.include_router(router)


@app.get('/')
def root():
    return {'message': 'Hello'}
