from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(route_name='home', renderer=__name__ + ':templates/mytemplate.pt')
def my_view(request):
    return {'project': 'singlefile'}


def includeme(config):
    config.add_static_view('static', '__main__:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan(__name__)


if __name__ == '__main__':
    # load the settings for the application
    settings = {}

    config = Configurator(settings=settings)
    config.include(__name__)
    app = config.make_wsgi_app()

    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
