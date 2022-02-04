class my_class():
   def __init__(self, o_x, o_y):
       self.x = o_x
       self.y = o_y
   def hello(self):
       print("hello there")
   def how(self):
       print("how are you doing?")

my_obj = my_class(5, 6)
print(my_obj)
print(my_obj.x, my_obj.y)
my_obj.hello()
my_obj.how()
