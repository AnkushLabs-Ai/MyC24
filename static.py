class Demo:
    a = 5    
    def _init_(self,b):
        self.b = b
    
    def test_function(self):
        print("This is a test test_function")

    # / @staticmethod # this is only an extra & doesn't change the O/P of the code but it is a good proactse to write it
    def my_function():
        print("this is my_function")

print(Demo.a)
d1= Demo(10)
print(d1.a)
d1.a =50
print(Demo.a)
