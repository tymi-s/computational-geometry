
def Heron(abc):

    if len(abc) !=3:
        print("TO NIE JEST TRÓJKĄT!!!")
        return

    a=abc[0]
    b=abc[1]
    c=abc[2]

    p = (a+b+c)/2
    field = (p*(p-a)*(p-b)*(p-c))**0.5

    return field


