class Square:
      def __init__(self):
          self.__height = 2
          self.__width = 2
    def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side

  square = Square()
  square.__height = 3 # raises AttributeError
  
#square = Square()
#square._Square__height = 3 # is allowed
