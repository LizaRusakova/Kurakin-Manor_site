import os

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = 27017

MONGO_DBNAME = 'rest'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'email': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True,
        'unique': True,
    },
    'mobile': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True,
        'unique': True,
    },
    'age': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'occupation': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'major': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'pros': {
        'type': 'list',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'cons': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'suggestions': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
}

people = {
    'item_title': 'person',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'email'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}

DOMAIN = {
    'people': people,
}
