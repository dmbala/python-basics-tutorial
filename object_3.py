
class my_class():
    def __init__(self):
        self.x = 2
        self.y = 3

    def hello(self):
        print("hello there")

    def how(self):
        print("how are you doing?")

my_obj = my_class()
print(my_obj)
print(my_obj.x, my_obj.y)
my_obj.hello()
my_obj.how()
