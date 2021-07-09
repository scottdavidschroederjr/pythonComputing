class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height  

  def get_area(self):
    area = self.width * self.height
    return area  

  def get_perimeter(self):
    perimter = (2 * self.width) + (2 * self.height)
    return perimter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      error = "Too big for picture."
      return error

    else:
      picture = ""
      countHeight = 0
      while countHeight < self.height:
        countWidth = 0
        while countWidth < self.width:
          picture = picture + "*"
          countWidth = countWidth + 1
        picture = picture + "\n"
        countHeight = countHeight + 1  
      return picture

  def get_amount_inside(self, shape):
    inside = self.get_area() / shape.get_area()
    return int(inside)


  def __str__(self):
    print = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return print

  
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    print = "Square(side=" + str(self.width) + ")"
    return print

              
