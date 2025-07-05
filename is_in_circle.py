from math import sqrt


def is_in_circle(r, x, y, points):

    min_dist = float('inf')
    closest_idx = -1

    for idx, point in enumerate(points):
        px, py = point
        dist = sqrt((x - px) ** 2 + (y - py) ** 2)

        if dist < min_dist:
            min_dist = dist
            closest_idx = idx

    if min_dist <= r:
        return True, closest_idx
    else:
        return False, -1