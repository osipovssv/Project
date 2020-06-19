class Abc:
     def __init__(self, x):
         self.x = x


a = Abc(10)
a.y = 20
print(a.x, a.y)

setattr(a, 'hello', 100)
print(a.hello)

attr = getattr(a, 'x')
print(attr)

attr = getattr(a, 'z', None)
print(attr)

print(hasattr(a, 'x'))
print(hasattr(a, 'bye'))
