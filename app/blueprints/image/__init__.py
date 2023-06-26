from flask.blueprints import Blueprint
from flask_restful import Api

from .image import Image

bp = Blueprint('image', __name__, url_prefix='/image')
api = Api(bp)
api.add_resource(Image, '')
