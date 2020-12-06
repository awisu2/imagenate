from imagenate.libs.enum import CustomEnum


class Sizes:
    """一般的によくあるサイズ

    H: horizontal(水平)
    V: vertical(垂直)
    """

    H8K = (7680, 4320)
    H4K = (3840, 2160)
    H2K = (1920, 1080)
    HHD = (1280, 720)

    V8K = (4320, 7680)
    V4K = (2160, 3840)
    V2K = (1080, 1920)
    VHD = (720, 1280)

    @classmethod
    def get(cls, key: str):
        if key == "hd":
            return cls.HHD
        elif key == "2k":
            return cls.H2K
        elif key == "4k":
            return cls.H4K
        elif key == "8k":
            return cls.H8K
        if key == "vhd":
            return cls.VHD
        elif key == "v2k":
            return cls.V2K
        elif key == "v4k":
            return cls.V4K
        elif key == "v8k":
            return cls.V8K
        return None
