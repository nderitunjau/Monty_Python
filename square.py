class Square:
      def __init__(self):
          self._height = 2
          self._width = 2
      def set_side(self, new_side):
          self._height = new_side
          self._width = new_side

  square = Square()
  square._height = 3 # not a square anymore
