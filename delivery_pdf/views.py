from aiohttp import web, ClientSession, ClientTimeout
import uuid


async def index(request):
    return web.Response(text="aiohttp status: on-line")


class CreatePDF:

    def __init__(self, server, servise):
        self.uuid_dict = {}
        self.server = server
        self.service = servise
        self.add_uuid = None

    def get_uuid(self):
        return str(uuid.uuid4())

    async def fetch_pdf(self, uuid):
        host_service = self.service['host']
        port_service = self.service['port']
        host_server = self.server['host']
        port_server = self.server['port']

        url = 'http://{}:{}/convert'.format(host_service, port_service)
        url_server = 'http://{}:{}/raw/{}'.format(host_server, port_server, uuid)
        params = {'auth': 'arachnys-weaver', 'url': url_server}
        timeout = ClientTimeout(total=6*60, connect=2*60, sock_connect=60, sock_read=60)
        async with ClientSession(timeout=timeout) as session:
            async with session.get(url=url, params=params) as resp:
                content = await resp.content.read()
                return content

    async def convert_html(self, request):
        if request.method == 'POST':
            content = await request.read()
            add_uuid = self.get_uuid()
            self.uuid_dict[add_uuid] = content
            pdf_content = await self.fetch_pdf(add_uuid)
            self.uuid_dict.pop(add_uuid)
            return web.Response(body=pdf_content, content_type='application/pdf')

    async def fetch_html(self, request):
        str_uuid = request.match_info['uuid']
        html = self.uuid_dict.get(str_uuid)
        if not html:
            web.HTTPNotFound()
        html_str = html.decode('utf-8')
        return web.Response(text=html_str)
