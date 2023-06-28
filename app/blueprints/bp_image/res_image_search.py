from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage


class ResImageSearch(Resource):
    """restful api for image similarity

    Args:
        Resource (_type_): _description_
    """

    # TODO: 图像文本搜索，接收字符串
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str, required=True,
                            help='query is required', location='args')
        data = parser.parse_args()

        return data.get('query')

    # TODO：图像相似搜索，接收图像文件
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', required=True, type=FileStorage,
                            help='file is required', location='files')
        data = parser.parse_args()

        return data.get('file').filename
