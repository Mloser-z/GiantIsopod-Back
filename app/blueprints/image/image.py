from flask_restful import Resource, reqparse


class Image(Resource):
    """Restful class

    Args:
        Resource (_type_): Parent Class
    """

    def __init__(self) -> None:
        super().__init__()

    # TODO: 返回已有的图像x个地址
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('index', type=int, required=True, location='args')
        data = parser.parse_args()
        index = data.get('index')

        return index

    # TODO： 返回图片详细信息
    def post(self):
        return None

    def put(self):
        return None

    def delete(self):
        return None
