def IW(p1,p2,p3):
    v1x = p2.x - p1.x
    v1y = p2.y - p1.y
    v2x = p3.x - p1.x
    v2y = p3.y - p1.y

    # Iloczyn wektorowy v1 × v2
    cross_product = v1x * v2y - v1y * v2x

    return cross_product