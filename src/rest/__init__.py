from flask import Blueprint
from flask_restplus import Api

TITLE = "House price prediction."
VERSION = "0.1.0"
DESCRIPTION = "API's for House price prediction"

from src.rest.resources import api as aa

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title=TITLE,
          version=VERSION,
          description=DESCRIPTION)

api.add_namespace(aa, path='')