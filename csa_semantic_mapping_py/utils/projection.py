# projection.py

import numpy as np
from .config import CAMERA_INTRINSICS

def deproject_pixel_to_point(u, v, depth):
    fx = CAMERA_INTRINSICS['fx']
    fy = CAMERA_INTRINSICS['fy']
    cx = CAMERA_INTRINSICS['cx']
    cy = CAMERA_INTRINSICS['cy']

    z = depth
    if z == 0:
        return None  # invalid point

    x = (u - cx) * z / fx
    y = (v - cy) * z / fy

    return (x, y, z)
