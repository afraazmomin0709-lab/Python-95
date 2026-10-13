class Sample:
  def get_data(me,a,b):
    me.n1=a
    me.n2=b
  def show(me):
    print(f"Value of n1:{me.n1}\nvalue of n2:{me.n2}")

s=Sample()
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
s.get_data(a,b)
s.show()