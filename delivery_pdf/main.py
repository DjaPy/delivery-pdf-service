from aiohttp import web

from .settings import config_t
from .routes import setup_routes
from .views import CreatePDF


async def init(argv=None):
    app = web.Application()
    server = config_t['server']
    service = config_t['service']
    handler = CreatePDF(server, service)
    setup_routes(app, handler)
    app['config'] = config_t['external']
    # host = config_t['external']['host']
    # port = config_t['external']['port']

    return app


def main():
    app = init()
    web.run_app(app)

