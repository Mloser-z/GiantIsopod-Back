class ImageBase:
    """base class for image
    """

    def __init__(self, url: str) -> None:
        """init instance with url

        Args:
            url (str): path to get image
        """
        self.url = url


class ImageBrief(ImageBase):
    """class for image with url and message
    """

    def __init__(self, url: str, message: str) -> None:
        """init instance with url and message

        Args:
            url (str): path to get image
            message (str): message of image
        """
        super().__init__(url)
        self.message = message


class ImageSimi(ImageBase):
    """Similarity information of one image
    """

    def __init__(self, url: str, label: str, similarity: float) -> None:
        """init instance with url, label, similarity

        Args:
            url (str): path to get image
            label (str): class of image
            similarity (float): similarity of image
        """
        super().__init__(url)
        self.label = label
        self.similarity = similarity
