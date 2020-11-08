from enum import Enum, IntEnum


class AccessTypes(IntEnum):
    """
    Enumeration for privacy definition of post or feed
    """
    PRIVATE = 0
    PUBLIC = 1

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class PostTypes(Enum):
    """
    Enumeration for defining the content type of a post
    """
    TEXT = 0, ('Text')
    IMAGE = 1, ('Image')
    VIDEO = 2, ('Video')


class ReactionTypes(Enum):
    """
    Enumeration for defining the reaction to a post
    """
    LIKE = 0, ('Like')
    SHARE = 1, ('Share')
