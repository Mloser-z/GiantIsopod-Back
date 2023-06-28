from flask_restful import Resource, reqparse


class ResLabel(Resource):
    """Restful class for label resource.

    Args:
        Resource (_type_): Parent Class
    """

    def __init__(self) -> None:
        super().__init__()

    # TODO: 返回所有类的简要信息List[ImageBrief]
    def get(self):

        return {"hello": "world"}

    # TODO： 返回类的详细信息
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('label', type=str, required=True,
                            help='label is required', location='json')
        data = parser.parse_args()

        return data.get('label')

    def put(self):
        return None

    def delete(self):
        return None
