from flask.blueprints import Blueprint
from flask_restful import Api

from .res_label import ResLabel
from .res_image_search import ResImageSearch


bp = Blueprint('bp_image', __name__, url_prefix='/image')
api = Api(bp)
api.add_resource(ResLabel, '/label')
api.add_resource(ResImageSearch, '/search')
