class LabelBase:
    """base class for label
    """

    def __init__(self, url: str, label: str) -> None:
        """init instance of LabelBase

        Args:
            url (str): path to get image
            label (str): class of image
        """
        self.url = url
        self.label = label


class Label(LabelBase):
    """class for label
    """

    def __init__(self, url: str, label: str, info: str, urls: list[str]) -> None:
        """init instance of Label

        Args:
            url (str): path to get image
            label (str): class of image
            info (str): detailed information
        """
        super().__init__(url, label)
        self.info = info
        self.urls = urls
