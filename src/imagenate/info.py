from PIL import Image


def get_info(file):
    image = Image.open(file)
    info = {
        "size": image.size,
        # 'P', 'RGBA', 'LA', 'L' の場合 jpegでは保存できないらしい
        "mode": image.mode,
        "filename": image.filename,
        "palette": image.palette,
        "info": image.info,
    }

    return info
