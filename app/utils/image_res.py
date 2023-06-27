class ImageBase:
    """base class for image
    """

    def __init__(self, url: str, label: str) -> None:
        """init instance with url, label

        Args:
            url (str): path to get image
            label (str): class of image
        """
        self.url = url
        self.label = label


class ImageBrief(ImageBase):
    """Brief information of one image

    Args:
        ImageBase (_type_): _description_
    """

    def __init__(self, url: str, label: str, message: str) -> None:
        """init instance with url, label, message

        Args:
            url (str): path to get image
            label (str): class of image
            message (str): additional information
        """
        super().__init__(url, label)
        self.message = message


class ImageSimi(ImageBase):
    """Similarity information of one image

    Args:
        ImageBase (_type_): _description_
    """

    def __init__(self, url: str, label: str, similarity: float) -> None:
        """init instance with url, label, similarity

        Args:
            url (str): path to get image
            label (str): class of image
            similarity (float): similarity of image
        """
        super().__init__(url, label)
        self.similarity = similarity


class ImagesRes:
    """List of ImageBrief for http return, used with json.dumps(xx.__dict__)
    """

    # TODO: 根据index和num来返回相应数量的图片数据，以及本次的index
    def __init__(self, index: int, num: int) -> None:
        """Init instance with url, label, message

        Args:
            index (int): index of last return
            num (int): number of images to return
        """
        self.images = []
        self.index = None

    # TODO: 根据index的位置来返回相应的图片数据
    def _get_image(self, index: int) -> ImageBrief:
        """Get image(url, label, message)

        Args:
            index (int): index of last return

        Returns:
            ImageBrief: brief information of image with index
        """
        pass


class ImageInfo:
    """Detailed information of one image getting from its label, used with json.dumps(xx.__dict__)
    """

    def __init__(self, label: str) -> None:
        """Init Instance with label

        Args:
            label (str): class of image
        """
        self.label = label
        self.info = self._get_info(label=label)

    # TODO: 根据label获取花朵详细信息
    def _get_info(self, label: str) -> str:
        """Get detailed information

        Args:
            label (str): class of image

        Returns:
            str: Detailed information
        """
        pass
