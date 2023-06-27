from flask_restful import Resource, reqparse


class ImageSimi(Resource):
    """restful api for image similarity

    Args:
        Resource (_type_): _description_
    """

    # TODO: 图像文本搜索，接收字符串
    def get(self):
        return {'hello': 'world'}

    # TODO：图像相似搜索，接收图像文件
    def post(self):
        return {'hello': 'world'}
