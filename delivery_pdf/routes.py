from .views import index


def setup_routes(app, handler):
    router = app.router
    h = handler
    router.add_get('/', index)
    router.add_get('/raw/{uuid}', h.fetch_html)
    router.add_post('/generate', h.convert_html)
