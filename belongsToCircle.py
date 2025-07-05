def BelongsToCircle(triangle_x, triangle_y, point_x, point_y):


    # if len(triangle_x) != 3 or len(triangle_y) != 3:
    #     raise ValueError("Trójkąt musi mieć dokładnie 3 wierzchołki")


    x1, x2, x3 = triangle_x
    y1, y2, y3 = triangle_y


    matrix = [
        [x1 - point_x, y1 - point_y, (x1 - point_x) ** 2 + (y1 - point_y) ** 2],
        [x2 - point_x, y2 - point_y, (x2 - point_x) ** 2 + (y2 - point_y) ** 2],
        [x3 - point_x, y3 - point_y, (x3 - point_x) ** 2 + (y3 - point_y) ** 2]
    ]


    det = (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

   # det>0 oznacza ze punkt lezy w ogregu
    return det > 0


