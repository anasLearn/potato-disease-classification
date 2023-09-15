from io import BytesIO

from PIL import Image
import numpy as np


def read_file_as_image(data) -> np.ndarray:
    """
    Transform an image file to numpy array
    Args:
        data: image file in Bytes type

    Returns:
        np array

    """
    image = np.array(Image.open(BytesIO(data)))
    return image
