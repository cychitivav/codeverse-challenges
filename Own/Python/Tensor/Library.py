class Matrix(list):
   rows = 0
   cols = 0
   obj = []

   def __init__(self, *args):
      self.rows = len(args)
      self.cols = len(args[0])
      for r in args:
         if len(r) != self.cols:
               raise Exception("Incorrect arguments")

      self.obj = list(args)

   def T(self):
      return [[self.obj[j][i] for j in range(self.rows)] for i in range(self.cols)]

   def determinant(self):
      if self.rows == self.cols:
         if self.rows == 1 and self.cols == 1:
               return self.obj[0]
         else:
               return 1
      else:
         return 0

   def det(self):
      return self.determinant()

   def inv(self):
      pass

   def adj(self):
      return 1

   def __contains__(self, element):
      for r in self.obj:
         if r == element:
               return True
         for c in r:
               if c == element:
                  return True

      return False

   def __add__(self, Addend):
      if self.rows == Addend.rows and self.cols == Addend.cols:
         return [[self.obj[i][j]+Addend.obj[i][j] for j in range(self.cols)] for i in range(self.rows)]
      else:
         return 0

   def __mul__(self, Multiplier):
      if self.cols == Multiplier.rows:
         return [[sum([self.obj[i][j]*Multiplier.obj[j][k] for j in range(self.cols)]) for k in range(Multiplier.cols)] for i in range(self.rows)]
      else:
         return 0

   def __truediv__(self, Divisor):
      return self.obj * Divisor.inv()


A = Matrix([1, 2], [3, 4], [5, 6])
B = Matrix([2, 5], [6, 7], [1, 8])
print(8 in A)
