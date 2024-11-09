class Rectangle:
    def __init__(self,length: int, breadth :int):
        if not isinstance(length, int) or not isinstance(breadth,int):
            raise TypeError("Length and Breadth must be integers")
        if length <= 0 or breadth <= 0:
            raise ValueError("Length and Breadth must be positive integers")
        self.length = length
        self.breadth = breadth
    
    def __iter__(self):
        yield{'length':self.length}
        yield{'breadth':self.breadth}

rect = Rectangle(5 ,15)

for change_in_dimension in rect:
    print(change_in_dimension)

