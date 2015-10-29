from pyramid.response import Response
from pyramid.view import view_config
from pyramid import request

from pyramid.httpexceptions import HTTPFound

# /contact


@view_config(route_name='contact', renderer='templates/contact.pt')
def contact(request):
    return {'name': 'Contact Form'}

# /banci


@view_config(route_name='sucursale', renderer='templates/banci.pt')
def sucursale(request):
    return {'name': 'Sucursale'}

# /detalii


@view_config(route_name='detalii', renderer='templates/detalii.pt')
def detalii(request):
    return {'name': 'Detalii'}
