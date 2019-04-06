import os
from pathlib import Path

from aiohttp import web
from dotenv import load_dotenv

from .routes import setup_routes
from .views import CreatePDF


env_path = Path('.') / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path)


async def init(argv=None):
    app = web.Application()
    server = {
        'host': os.getenv('SERVER_HOST'),
        'port': os.getenv('SERVER_PORT')
    }
    service = {
        'host': os.getenv('SERVICE_HOST'),
        'port': os.getenv('SERVICE_PORT')
    }
    handler = CreatePDF(server, service)
    setup_routes(app, handler)
    app['config'] = {
        'host': os.getenv('SERVICE_HOST'),
        'port': os.getenv('SERVER_PORT'),
    }

    return app


def main():
    app = init()
    web.run_app(app)

