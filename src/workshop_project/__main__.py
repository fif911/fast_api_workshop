"""
Файл который использует пайчарм чтобы запускать сервак
"""
import uvicorn

from .settings import settings

uvicorn.run(
    'workshop_project.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
