from coroweb import get, post

@get('/')
def index(request):
    return web.Response(body=b'<h1>Awesome!</h1>', content_type='text/html')

