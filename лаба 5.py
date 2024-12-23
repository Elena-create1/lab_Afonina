#задание 1
class Book:
    def __init__(self, title, author, date):
        self.title=title
        self.author=author
        self.date=date
    def get_info(self):
        return f"название: {self.title}, автор: {self.author}, год выпуска: {self.date}"
a=Book('Капитанская дочка','А.С.Пушкин',1836)
print(a.get_info())


#задание 2
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def get_radius(self):
        return f"радиус круга: {self.radius}"
    def set_radius(self, new_radius):
        self.radius=new_radius
c=Circle(5)
c.set_radius(12)
print(c.get_radius())
