class Point:
    def __init__(self,idd,x,y):
        self.idd = idd
        self.x = x
        self.y = y
        
    def printing(self):
        print(f"Point {self.idd} is at ({self.x},{self.y})")