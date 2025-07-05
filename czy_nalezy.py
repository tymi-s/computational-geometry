
def czy_nalezy_do_prostej(a,b,x,y):
    if y == (a*x +b):
        print(f"\npunkty {x},{y} nalezy do prostej {a}x + {b}!")
    else:
        print(f"\npunkty {x},{y} NIE nalezy do prostej {a}x + {b}!")