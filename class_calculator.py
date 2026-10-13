class Calculator:
  def __init__(self):
      self.n1=10
      self.n2=20

  def add(self):
      print(f"Addition of {self.n1} and {self.n2} = {self.n1+self.n2}")

  def sub(self):
      print(f"Substraction of {self.n1} and {self.n2} = {self.n1-self.n2}")

  def multi(self):
      print(f"Multiplication of {self.n1} and {self.n2} = {self.n1*self.n2}")

  def div(self):
      print(f"Division of {self.n1} and {self.n2} = {self.n1/self.n2}")

  def float_div(self):
      print(f"Float Division of {self.n1} and {self.n2} = {self.n1//self.n2}")

  def module(self):
      print(f"Modulo of {self.n1} and {self.n2} = {self.n1%self.n2}")

c=Calculator()
c.add()
c.sub()
c.multi()
c.div()
c.float_div()
c.module()